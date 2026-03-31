Since newer versions (Django 4+), logout requires POST for security reasons:

Prevents malicious sites from logging users out automatically
Protects against CSRF attacks

profile creation:

 We will be creating a user profile that extends the built-in Django User model. We will then use this user profile to store profile pictures for each user. We will also be learning how to set the MEDIA_ROOT, MEDIA_URL, and also make our static files accessible through our URL patterns. Finally, we will create a receiver function for a Django signal that will make sure our profiles are created when a user first registers. 

You have to install pillow in order allow image functionalities 


in the case that signals.py causes an error from initialy created profiles run from django.contrib.auth.models import User
>>> from users.models import Profile
>>> for user in User.objects.all():
...     Profile.objects.get_or_create(user=user)
in shell (python manage.py shell)