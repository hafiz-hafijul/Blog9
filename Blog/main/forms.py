from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Post, Category, ContactModel, CommentModel
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [ 'keyword','title',]
        widgets = {
            'keyword':forms.TextInput(attrs={'class':'form-control ','placeholder':'keyword for seo'}),
            'title':forms.TextInput(attrs={'class':'form-control ','placeholder':'Category'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['keyword', 'description','category', 'title','content','email','image']
        widgets = {
            'keyword': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'keyword for seo'}),
            'description': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'description for seo'}),
            'category': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Category'}),
            'title': forms.TextInput(attrs={'class': 'form-control '}),
            'content': forms.Textarea(attrs={'class': 'form-control '}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields=['name','email','subject','message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control ', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Message'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'email', 'subject','phone', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Your Name', 'id': 'contact_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control ', 'placeholder': 'Your Email', 'id': 'contact_email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Subject', 'id': 'contact_email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder': 'Your Phone Number', 'id': 'contact_sphone'}),
            'text': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Please Comment Here ...', 'id': 'message', "name":"commentid"}),
        }

        def commt(self):
            data=CommentModel()
            data.name=self.cleaned_data['name']
            data.email=self.cleaned_data['email']
            data.subject=self.cleaned_data['subject']
            data.phone=self.cleaned_data['phone']
            data.text=self.cleaned_data['text']
            data.save()
            return data

