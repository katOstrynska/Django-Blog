# Generated by Django 2.0 on 2017-12-28 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_sth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_bot',
            new_name='is_bot_flag',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]
