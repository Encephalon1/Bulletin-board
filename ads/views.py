from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *


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
    template_name = 'ad_one.html'
    context_object_name = 'replies'
