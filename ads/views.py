from django.shortcuts import render, get_object_or_404
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
        return super().form_valid(form)
