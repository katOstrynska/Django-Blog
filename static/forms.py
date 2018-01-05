from django import forms

from .models import Post, Blogimg

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'image' , 'content',)

class BlogimgForm(forms.ModelForm):

    class Meta:
        model = Blogimg
        fields = ('upload_title', 'upload_image',)