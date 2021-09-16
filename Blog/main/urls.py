from django.urls import path
from main import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('category_list/<slug:category_slug>/', views.category_list, name='category_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('create/', views.categoryview, name='create'),
    path('single/<slug:slug>/', views.post_details, name='single'),
    path('likes/<int:id>/', views.likepost, name='likes'),
]
