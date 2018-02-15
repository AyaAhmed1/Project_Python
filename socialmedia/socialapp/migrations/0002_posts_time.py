# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 15, 38, 24, 734458, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
