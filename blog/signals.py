from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from blog.jobs import bot
import random
from redis import Redis
from rq_scheduler import Scheduler
from datetime import timedelta

scheduler = Scheduler(connection=Redis())


@receiver(post_save, sender=Post)
def bot_create_comments(sender, instance, created, **kwargs):
    # delay() - job pushed to queue instant after post_save
    # bot.delay(instance.id)
    # scheduler - job pushed to queue after timedelta after post_save
    scheduler.enqueue_in(timedelta(minutes=random.randint(0, 2)), bot, instance.id)
