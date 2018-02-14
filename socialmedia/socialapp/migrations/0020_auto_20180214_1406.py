# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0019_auto_20180214_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='img',
            field=models.CharField(default=b'1.jpeg', max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='imag',
            field=models.ImageField(default=b'1.jpeg', upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(to='socialapp.Comment'),
        ),
    ]
