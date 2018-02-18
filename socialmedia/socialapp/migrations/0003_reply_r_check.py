# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0002_auto_20180217_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='R_check',
            field=models.IntegerField(default=0),
        ),
    ]
