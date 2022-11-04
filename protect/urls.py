from django.urls import path
from .views import IndexView, get_replies


urlpatterns = [
    path('', IndexView.as_view()),
    path('cabinet/', get_replies, name='get_replies')
]
