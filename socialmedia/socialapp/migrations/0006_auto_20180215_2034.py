# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_auto_20180215_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(default=b'1.jpeg', upload_to=b'./static/', blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
