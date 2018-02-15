# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0014_auto_20180215_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='imag',
            new_name='img',
        ),
    ]
