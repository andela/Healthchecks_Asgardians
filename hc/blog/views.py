from django.shortcuts import render, redirect, get_object_or_404
from hc.blog.models import Post
from django.utils import timezone
from .forms import PostForm


def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_view', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/create_post.html', {'form': form})


def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_page.html', {'post': post})
