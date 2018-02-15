# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0004_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.CharField(max_length=255),
        ),
    ]
