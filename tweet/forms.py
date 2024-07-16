from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title','text', 'photo']  # include all the fields you want in the form


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class META:
        model = User
        field=('username','email','password1','password2')