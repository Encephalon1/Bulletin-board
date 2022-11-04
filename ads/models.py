from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Ad(models.Model):
    title = models.CharField(max_length=100)
    ad_text = models.TextField()
    date_and_time_of_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.ImageField(blank=True, null=True, upload_to='content')

    def get_absolute_url(self):
        return reverse('single_ad', args=[str(self.id)])


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    resp_text = models.TextField()
    accept_reply = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('single_ad', args=[str(self.id)])

