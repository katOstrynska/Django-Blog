# import requests
# from django_rq import job
#
# from .models import Post, Comment
#
#
# # @job
# # def count_words_at_url(url):
# #     resp = requests.get(url)
# #     return len(resp.text.split())
#
# # @job
# def add(x, y):
#     print("The output is: ", x + y)
#
#
# def bot():
#     posts_with_comments = Comment.objects.all().values_list('post_id', flat=True)
#     print(posts_with_comments)
#     posts_without_comments = Post.objects.exclude(id__in=posts_with_comments).values_list('id', flat=True)
#     print(posts_without_comments)
#     for id in posts_without_comments:
#         Comment.objects.create(post_id=id, author='AuthorKasia', text='Nowy komentarz')