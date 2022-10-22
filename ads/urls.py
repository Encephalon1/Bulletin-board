from django.urls import path
from .views import *


urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', SingleAd.as_view(), name='single_ad')
]
