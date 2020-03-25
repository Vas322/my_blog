from django import forms
from .models import Post, Entry


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
