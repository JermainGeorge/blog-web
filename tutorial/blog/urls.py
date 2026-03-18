
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('Login/', views.Login, name='blog-Login'),
    path('Register/', views.Register, name='blog-Register'),
]