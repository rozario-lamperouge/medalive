from django.shortcuts import render, redirect
from .forms import AdminSignUpForm
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Media
from .serializers import PostSerializer, MediaSerializer, PostSerializerList

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_signup_success')
    else:
        form = AdminSignUpForm()
    groups = Group.objects.all()
    return render(request, 'admin_signup.html', {'form': form, 'groups': groups})

def admin_signup_success(request):
    return render(request, 'admin_signup_success.html')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerList
    permission_classes = []

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

