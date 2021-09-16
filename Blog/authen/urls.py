from django.urls import path
from authen import views

urlpatterns = [
    path('sign/', views.UserSignView.as_view(), name='sign'),
    # path('login/', views.UserLoginView.as_view(), name='login'),
    path('login/', views.userlogin, name='login'),
    # path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/<slug:profile_slug>', views.getProfile, name='profile'),
]
