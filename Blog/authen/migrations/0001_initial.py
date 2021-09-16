# Generated by Django 3.2.3 on 2021-09-13 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='profile/profile.png', null=True, upload_to='profile/User_profile')),
                ('cover_image', models.ImageField(blank=True, default='profile/profile.png', null=True, upload_to='profile/user_cover_profile')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='profile/profile.png', null=True, upload_to='profile/admin_profile')),
                ('cover_image', models.ImageField(blank=True, default='profile/profile.png', null=True, upload_to='profile/admin_cover_profile')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
