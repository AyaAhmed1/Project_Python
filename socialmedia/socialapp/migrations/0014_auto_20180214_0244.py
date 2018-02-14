# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0013_auto_20180214_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='dislike',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='like',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
    ]
