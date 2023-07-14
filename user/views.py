from django.shortcuts import render, redirect
from .forms import AdminSignUpForm

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_signup_success')
    else:
        form = AdminSignUpForm()
    return render(request, 'admin_signup.html', {'form': form})

def admin_signup_success(request):
    return render(request, 'admin_signup_success.html')
