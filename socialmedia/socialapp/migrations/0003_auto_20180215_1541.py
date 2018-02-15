# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0002_posts_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='p_body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='tag',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
