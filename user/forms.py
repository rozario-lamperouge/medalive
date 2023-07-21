from django import forms
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.conf import settings

class AdminSignUpForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    user_group = forms.ModelChoiceField(queryset=Group.objects.all())
    print(Group.objects.all())

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        user_group = self.cleaned_data['user_group']
        password = User.objects.make_random_password()

        user = User.objects.create_superuser(username=username, password=password, email=email)
        user.groups.add(user_group)

        print(username,email,password)
        Recipient = [email]
        sender = 'richardrozario.a@gmail.com'
        
        message = f"Please Save Your Credentials for admin login" + "\n " + "Username: " + username + "\n " + "Password: " + password
        send_mail('Admin Account Created', message, sender, Recipient)
