from django.shortcuts import render

posts = [
    {
        'author':'Jermain Geo',
        'Title':'Blog post 1',
        'content':'All about code ' ,
        'date_posted':'october 20th 2024', 

    },
    {
        'author':'Jermain Geo',
        'Title':'Blog post 2 ',
        'content':'All about code2 ' ,
        'date_posted':'october 21th 2024', 

    }
]

def home(request):

    context = {'posts':posts
               }

    return render (request, 'blog/home.html',context)
    

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

def Login(request):
    return render(request,'blog/Login.html',{'title': 'Login'})

def Register(request):
    return render(request,'blog/Register.html',{'title': 'Register'})