from django.contrib import admin


from .models import Post, Blogimg, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Blogimg)


