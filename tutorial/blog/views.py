from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post

def home(request):

    context = {'posts':Post.objects.all()
               }

    return render (request, 'blog/home.html',context)
    

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

def login(request):
    return render(request , 'blog/login.html', {'title':'Login'})


def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)

    context = {
        'view_user': user,
        'posts': posts
    }
    return render(request, 'blog/user_posts.html', context)