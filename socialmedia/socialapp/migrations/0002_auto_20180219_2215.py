# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='like',
        ),
        migrations.AddField(
            model_name='posts',
            name='countdislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='countlike',
            field=models.IntegerField(default=0),
        ),
    ]
