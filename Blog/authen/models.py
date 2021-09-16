from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='profile/admin_profile', default='profile/profile.png', blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='profile/admin_cover_profile', default='profile/profile.png', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


    def cont(self):
        return self.content[:50]
    
    def ab_img(self):
        if self.image:
            return self.image.url
        else:
            return ''
    
    def get_absolute_url(self):
        return reverse("profile", args=[self.slug])
    


class User_Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='profile/User_profile', default='profile/profile.png', blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='profile/user_cover_profile', default='profile/profile.png', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


    def cont(self):
        return self.content[:50]
    
    def ab_img(self):
        if self.image:
            return self.image.url
        else:
            return ''
    
    def get_absolute_url(self):
        return reverse("profile", args=[self.slug])
