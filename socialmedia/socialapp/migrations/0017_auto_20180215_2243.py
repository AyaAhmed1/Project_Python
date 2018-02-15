# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0016_auto_20180215_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='P_tag',
        ),
        migrations.AddField(
            model_name='posts',
            name='tag',
            field=models.CharField(default=datetime.datetime(2018, 2, 15, 22, 43, 41, 887151, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
