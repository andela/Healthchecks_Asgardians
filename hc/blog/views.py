from django.shortcuts import render, redirect, get_object_or_404
from hc.blog.models import Post, Category
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostForm

CATEGORIES_DATA = Category.objects.all()

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
        return render(request, 'blog/create_post.html', {"categories": CATEGORIES_DATA})


def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_page.html', {'post': post})


def blogs(request):
    posts = list(Post.objects.all())
    latest = posts[:2]
    other_posts = posts[3:]
    ctx= {
        "page": "blog",
        "posts": other_posts,
        "latest": latest,
        "categories": CATEGORIES_DATA
    }
    return render(request, 'blog/all_blogs.html', ctx)
