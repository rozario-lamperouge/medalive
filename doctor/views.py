from django.shortcuts import render, redirect
from user.models import Post, Media
from .forms import PostForm, LoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from user.serializers import PostSerializer, MediaSerializer
import time

def homeView(request):
    return render(request, 'home.html')

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_groups = user.groups.all()
            if user_groups.filter(name='Doctor').exists() or user_groups.filter(name='Vendor').exists():
                csrf = get_token(request)
                return JsonResponse({'status': 'success','token': csrf})
            else:
                return JsonResponse({'status': 'error'})
        else:
            return JsonResponse({'status': 'error'})
    
        return JsonResponse({'message': 'Incorrect username or password'})
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        uname = request.user.username
        logout(request)
        return JsonResponse({'message': 'Logout successful', 'user': uname})


def loginView(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            user_groups = user.groups.all()
            if user_groups.filter(name='Doctor').exists() or user_groups.filter(name='Vendor').exists():
                return render(request, 'home.html')
            else:
                return render(request, 'login.html')

    else:
        return render(request, 'login.html')
    

class CreatePostAPIView(APIView):
    def post(self, request):
        username = request.data.get('author')
        user = User.objects.get(username=username)
        request.data['author'] = user

        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
        }
        
        serializer = PostSerializer(data=data)
        print(serializer.is_valid())

        if serializer.is_valid():
            post = serializer.save(author=user)

            medias = request.FILES.getlist('medias')
            for media in medias:
                media_instance = Media(media=media)
                media_instance.save()
                post.medias.add(media_instance)
                

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_post(request):
    user = request.user
    if not user.groups.filter(name='Doctor').exists() or user.groups.filter(name='Vendor').exists():
        return render(request, '404.html')

    if request.method == 'POST':
        medias = request.FILES.getlist('medias')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            for media in medias:
                media = Media(media=media)
                media.save()
                post.medias.add(media)

            post.save()
            time.sleep(2)
            # return redirect('post', pk=post.pk)
            return render(request, 'post.html', {'post': post})
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
