from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,AuthenticationForm, UsernameField
from django.forms import widgets
from django.utils.translation import gettext, gettext_lazy as _
from .models import Profile



class UserForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirm ( Again )', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','content','image']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Complete Name'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'About Yourself'}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':'Your Complete Name'}),
        }