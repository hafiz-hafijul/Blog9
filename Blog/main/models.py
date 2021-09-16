from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.utils.safestring import mark_safe
import uuid
from django.utils import timezone


class Category(models.Model):
    keyword = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def slug_title(self):
        return self.slug+str(uuid.uuid4())

    def get_absolute_url(self):
        return reverse("category_list", args=[self.slug])


class Post(models.Model):
    keyword = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    content = models.TextField()
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(
        upload_to='post', default='post/default.jpg', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_like')
    view = models.ManyToManyField(User, related_name='post_view')
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def show_img(self):
        if self.image:
            return mark_safe('<img src="{}" heights="50px" width="40px" />'.format(self.image.url))
        else:
            return self.image
    show_img.short_description = 'Image'

    def img_url(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def desc(self):
        return self.description[:20]

    def title_tag(self):
        return self.title[:20]

    def cont(self):
        return self.content[:50]

    def slug_title(self):
        return self.slug + '-' + str(uuid.uuid4())

    def total_likes(self):
        return self.likes.count()

    def total_view(self):
        return self.view.count()

    class Meta:
        ordering = ['-created_at']


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def mess(self):
        return self.message[:50]

    def slug_name(self):
        return self.slug + str(uuid.uuid4())

    class Meta:
        ordering = ['-created_at']


class About(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='profile', default='profile/default.jpg', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)


    def cont(self):
        return self.content[:50]

    def ab_img(self):
        if self.image:
            return self.image.url
        else:
            return ''


class ContactDetail(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='profile', default='profile/default.jpg', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    

    def cont(self):
        return self.content[:50]

    def cont_img(self):
        if self.image:
            return self.image.url
        else:
            return ''


class CommentModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comment')
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=1020)
    email = models.EmailField()
    phone=models.PositiveIntegerField()
    text = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def commt(self):
        return self.text

