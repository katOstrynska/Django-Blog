from django.contrib import admin
from blog.models import Post, Blogimg, Comment, User


class UserAdmin(admin.ModelAdmin):
    model = User
    filter_horizontal = ('user_permissions', 'groups',)


admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Blogimg)


