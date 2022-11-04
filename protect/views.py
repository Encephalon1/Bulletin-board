from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ads.models import *


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'


@login_required
def get_replies(request):
    context = {
        'my_replies': Reply.objects.filter(ad__author=request.user)
    }
    return render(request, 'protect/cabinet.html', context)
