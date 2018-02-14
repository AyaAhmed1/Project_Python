# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0007_auto_20180214_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='like',
            field=models.IntegerField(default=b''),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
    ]
