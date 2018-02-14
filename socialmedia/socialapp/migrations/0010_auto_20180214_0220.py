# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0009_auto_20180214_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
    ]
