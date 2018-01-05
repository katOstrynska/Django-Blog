from django import forms

from .models import Post, Blogimg, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'image', 'content')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')


class BlogimgForm(forms.ModelForm):

    class Meta:
        model = Blogimg
        fields = ('upload_title', 'upload_image',)