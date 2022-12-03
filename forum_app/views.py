from django.shortcuts import render
from .models import Post, Comment
from django.contrib.auth.models import User
def index(request):
    posts = Post.objects.all().order_by('-date')
    context = {'posts':posts}
    return render(request, 'forum_app/index.html', context)


def create_post(request):
    if request.method  == 'POST':
        author = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        create_post = Post.objects.create(title = title, description = description, author = author)
    return render(request, 'forum_app/create_post.html')

def post(request, pk):
    post_comment = Post.objects.get(id = pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        post_comment = Comment.objects.create(post = post_comment, author = user, comment = comment)

    post = Post.objects.filter(id = pk)
    post_comment = Post.objects.get(id = pk)
    comment = Comment.objects.filter(post = post_comment)
    context = {'post':post, 'comments':comment}
    return render(request, 'forum_app/post.html', context)
def account(request, pk):
    user = User.objects.filter(id = pk)
    context = {'user':user}
    return render(request, 'forum_app/account.html', context)
