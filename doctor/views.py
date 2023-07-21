from django.shortcuts import render, redirect
from user.models import Post
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # return redirect('post', pk=post.pk)
            return render(request, 'post.html', {'post': post})
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
