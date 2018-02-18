# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialapp', '0018_auto_20180215_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cateusr',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(
            model_name='posts',
            name='dislike',
        ),
        migrations.AddField(
            model_name='posts',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.RemoveField(
            model_name='posts',
            name='like',
        ),
        migrations.AddField(
            model_name='posts',
            name='like',
            field=models.ManyToManyField(related_name='like', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
