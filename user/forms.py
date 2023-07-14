from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

class AdminSignUpForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = User.objects.make_random_password()

        User.objects.create_superuser(username=username, password=password, email=email)
        print(username,email,password)
        Recipient = [email]
        sender = 'richardrozario.a@gmail.com'
        message = f"Please Save Your Credentials for admin login" + "\n " + "Username: " + username + "\n " + "Password: " + password
        send_mail('Admin Account Created', message, sender, Recipient)
