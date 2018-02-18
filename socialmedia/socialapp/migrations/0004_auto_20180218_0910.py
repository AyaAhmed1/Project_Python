# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_reply_r_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='R_check',
        ),
        migrations.AddField(
            model_name='comment',
            name='R_check',
            field=models.IntegerField(default=0),
        ),
    ]
