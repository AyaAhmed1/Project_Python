# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0018_auto_20180214_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='img',
        ),
        migrations.AddField(
            model_name='posts',
            name='imag',
            field=models.ImageField(default=b'cheetos.jpeg', upload_to=b'static/img/', blank=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
    ]
