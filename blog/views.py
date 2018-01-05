from django.utils import timezone
from .models import Post, Blogimg

# from annoying.decorators import render_to
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .forms import PostForm, CommentForm

from django.shortcuts import redirect
from django.http import Http404

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .decorators import user_is_post_author

from django.shortcuts import render_to_response
from django.template import RequestContext


def handler403(request):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})
    # return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'post_detail.html', {'post': post})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
    # return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
        # pk=post.pk
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
    # return render(request, 'blog/post_edit.html', {'form': form})


@user_is_post_author
def post_edit(request, pk):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404

    post = get_object_or_404(Post, pk=pk)
    # if request.user != post.author:
    #     raise Http404
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

# return render(request, 'blog/post_edit.html', {'form': form})
#
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
#
#
# @login_required
# def home(request):
#     return render(request, 'home.html')

