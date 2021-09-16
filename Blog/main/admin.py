from django.contrib import admin
from .models import Category, Post, ContactModel, About, CommentModel,ContactDetail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'keyword', 'title', 'slug_title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ['js/tinyedit.js']
        
    list_display = ['keyword', 'desc', 'category',
                    'title_tag', 'email', 'cont', 'publish', 'show_img', 'slug_title']
    exclude=['author']
    search_fields = ['title_tag', 'author']
    list_filter = ['author', 'created_at']
    prepopulated_fields = {'slug': ['title']}

    


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'mess', 'slug_name']
    search_fields = ['name', 'email']
    list_filter = ['created_at', ]
    prepopulated_fields = {'slug': ['name']}


@admin.register(ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'image']
    exclude = ['user']
    list_filter = ['created_at', ]
    prepopulated_fields = {'slug': ['content']}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    class Media:
        js = ['js/tinyedit.js']
    exclude = ['user']
    list_display = ['id', 'content', 'image']
    list_filter = ['created_at', ]
    prepopulated_fields = {'slug': ['content']}




@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','subject', 'phone','text']
    search_fields = ['name',"phone" ]
    list_filter = ['created_at', ]
