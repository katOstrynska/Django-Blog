#!/usr/bin/env python
# -*- coding: utf-8 -*-
import django_rq
import random
from django_rq import job
from blog.models import Comment, User, Post

redis_conn = django_rq.get_connection('default')


@job
def bot(instance_id):
    posts_number = Post.objects.count()
    bot_users_number = User.objects.filter(is_bot_flag=True).count()
    name_parts_list = ['wiz', 'fiz', 'kat', 'pok', 'ker', 'aaw', 'tyn']
    posts_with_comments = Comment.objects.filter(post_id=instance_id).count()
    print(posts_with_comments)
    if posts_with_comments == 0:
        if posts_number > bot_users_number*3:
            bot_username = ''.join(random.sample(name_parts_list, 2))+str(random.randint(5, 87))
            new_author = User.objects.create(username=bot_username,
                                             password='djangoBot',
                                             is_bot_flag=True)
            new_author.save()
            new_comment = Comment.objects.create(post_id=instance_id,
                                                 author=new_author,
                                                 text='W pełni działający komentarz',
                                                 bot_name=new_author)
            print(new_comment)
        else:
            print('Wybieramy autora z najmniejszą liczbą komentarzy')
    else:
        print('Komentarz już jest')


