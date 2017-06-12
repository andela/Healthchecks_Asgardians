from django.shortcuts import render, redirect, get_object_or_404
from hc.blog.models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostForm

CATEGORIES = ["Design", "Programming", "Ne Technologies", "New Technologies", "UI/UX", "Cron jobs", "Others"]

@login_required()
def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = Post()
        post.author = request.user
        post.published_date = timezone.now()
        post.category = form.cleaned_data['category']
        post.content = form.cleaned_data['content']
        post.title = form.cleaned_data['title']
        post.save()
        return redirect('post_view', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/create_post.html', {"categories": CATEGORIES})


def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_page.html', {'post': post})


def blogs(request):
    posts = list(Post.objects.all())
    latest = posts[:2]
    ctx= {
        "page": "blog",
        "categories": CATEGORIES,
        "posts": posts,
        "latest": latest
    }
    return render(request, 'blog/all_blogs.html', ctx)
