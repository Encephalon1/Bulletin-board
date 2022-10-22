from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=20)


class Ad(models.Model):
    title = models.CharField(max_length=100)
    ad_text = models.TextField()
    date_and_time_of_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True, null=True)


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    resp_text = models.TextField()
    accept_reply = models.BooleanField(default=False)
