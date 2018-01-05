from django.conf import settings
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField

class Blogimg(models.Model):
    upload_author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_DEFAULT)
    upload_title = models.CharField(max_length=200)
    upload_date = models.DateTimeField(default=timezone.now)
    upload_alt = models.CharField(max_length=200, default='Alt Attribute For Image')
    upload_image = models.ImageField(upload_to='blogImg/%Y/%m/%d/', height_field=None, width_field=None, max_length=100, default='blogImg/2017/11/21/david-klaasen-54203.jpg')

    def publish(self):
        self.upload_date = timezone.now()
        self.save()

    def __str__(self):
        return self.upload_title


class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_DEFAULT)
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ManyToManyField(Blogimg)
    content = RichTextField(default='ckEditorString')
    excerpt = models.CharField(max_length=200, default='newValueString')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.SET_DEFAULT, default=1)
    author = models.CharField(max_length=200)
    text = RichTextField(default='Comment')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

