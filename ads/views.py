from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import AdForm, ReplyForm


class AdsList(ListView):
    model = Ad
    ordering = '-date_and_time_of_creation'
    template_name = 'ads_list.html'
    context_object_name = 'ads'
    paginate_by = 10


class SingleAd(DetailView):
    model = Ad
    template_name = 'ad_one.html'
    context_object_name = 'ad'


class RepliesView(ListView):
    model = Reply
    template_name = 'replies.html'
    context_object_name = 'replies'


class AdCreate(CreateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'

    def home(self, request):
        images = Ad.objects.all()
        context = {
            'images': images
        }
        return render(request, 'ad_edit.html', context)

    def file_upload(self, request):
        if request.method == 'POST':
            my_files = request.FILES.get('file')
            Ad.objects.create(content=my_files)
            return HttpResponse('ads/img/')
        return JsonResponse({'post': 'fasle'})

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        return super().form_valid(form)


class ReplyCreate(CreateView):
    form_class = ReplyForm
    model = Reply
    template_name = 'reply_edit.html'

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.author = self.request.user
        ad_id = self.kwargs['pk']
        reply.ad = get_object_or_404(Ad, id=ad_id)
        mail_user = Ad.objects.get(id=ad_id).author.email
        send_mail(
            subject='Reply',
            message='Вы получили отклик на ваше объявление. Вы можете посмотреть его в своем личном кабинете',
            from_email='viizdevaetes@mail.ru',
            recipient_list=[mail_user]
        )
        return super().form_valid(form)


def take_reply(request, pk):
    reply = Reply.objects.select_related('ad').get(ad__id=pk)
    reply.accept_reply = True
    reply.save()
    return redirect('/')
