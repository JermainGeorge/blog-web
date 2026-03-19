from django.shortcuts import render
from .models import Post

def home(request):

    context = {'posts':Post.objects.all()
               }

    return render (request, 'blog/home.html',context)
    

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

def Login(request):
    return render(request,'blog/Login.html',{'title': 'Login'})

def Register(request):
    return render(request,'blog/Register.html',{'title': 'Register'})