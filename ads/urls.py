from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', SingleAd.as_view(), name='single_ad'),
    path('<int:pk>/replies', RepliesView.as_view(), name='repl'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/replies/create/', ReplyCreate.as_view(), name='repl_create'),
    path('img/', AdCreate.home, name='home'),
    path('upload/', AdCreate.file_upload),
    path('take_reply', take_reply, name='take_reply')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
