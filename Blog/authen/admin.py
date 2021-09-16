from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'image', 'slug']
    search_fields = ['name', ]
    list_filter = ['created_at', ]
    prepopulated_fields = {'slug': ['name']}
