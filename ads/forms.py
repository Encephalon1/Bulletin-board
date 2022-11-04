from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *


class AdForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Ad
        content = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = [
            'title',
            'ad_text',
            'category',
            'content'
        ]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'resp_text'
        ]
