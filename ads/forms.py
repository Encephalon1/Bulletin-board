from django import forms
from .models import *


class AdForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    content = forms.FileInput

    class Meta:
        model = Ad
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
