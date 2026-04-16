from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterform, UserUpdateForm, ProfileUpdateForm



from django.core.mail import send_mail
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            #this will creat a new user from the form in the front end 
            user =form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ure account has been created you are now able to log in!')
            send_mail(
                subject='Welcome to the App',
                message=f'Hi {user.username}, your account has been created successfully.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
            return redirect('users-login')
    else:
        form = UserRegisterform()
    return render(request , 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ure account has been updated!')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request ,'users/profile.html',context)
