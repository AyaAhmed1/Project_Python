# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_auto_20180215_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 16, 23, 35, 902365, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
