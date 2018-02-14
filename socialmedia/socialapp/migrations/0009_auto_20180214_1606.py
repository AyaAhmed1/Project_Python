# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0008_auto_20180214_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 14, 16, 6, 18, 202443, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
    ]
