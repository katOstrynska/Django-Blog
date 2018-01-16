#!/usr/bin/env python
# -*- coding: utf-8 -*-
import django_rq
import random
from django_rq import job
from blog.models import Comment, User, Post
from django.db.models import Count

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
            # print('Wybieramy autora z najmniejszą liczbą komentarzy')
            # dict = {}
            bots_with_comments = User.objects.filter(is_bot_flag=True).annotate(num_comm=Count('comments'))
            tmp = bots_with_comments[0]
            for i in range (1,len(bots_with_comments)):
                if bots_with_comments[i].num_comm < tmp.num_comm:
                    tmp = bots_with_comments[i]
                if tmp.num_comm == 0:
                    break

            new_comment = Comment.objects.create(post_id=instance_id,
                                                 author=tmp,
                                                 text='W pełni działający komentarz wstawiony przez bota, który już istanieje w bazie',
                                                 bot_name=tmp)
            print(new_comment)

            # bots_with_comments = User.objects.filter(is_bot_flag=True).annotate(num_comm=Count('comments'))
            # for x in bots_with_comments:
            #     dict.update({x.username: x.num_comm})
            # print(dict)
            # bot_username_min_comments = min(dict, key=dict.get)
            # new_comment = Comment.objects.create(post_id=instance_id,
            #                                      author=bot_username_min_comments,
            #                                      text='W pełni działający komentarz wstawiony przez bota, który już istanieje w bazie')
            # print(new_comment)
    else:
        print('Komentarz już jest')


