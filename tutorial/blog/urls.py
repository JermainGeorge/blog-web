from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>/', views.user_posts, name='user-posts'),
    
]