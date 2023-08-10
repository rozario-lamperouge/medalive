from django import forms
from user.models import Post
from django.contrib.auth.models import User, Group

class PostForm(forms.ModelForm):
    medias = forms.FileField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'medias']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
