# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0010_auto_20180215_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.FileField(default=b'1.jpeg', null=True, upload_to=b'static/img', blank=True),
        ),
    ]
