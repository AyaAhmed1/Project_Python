# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='id_comment',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='time_replay',
            new_name='time_reply',
        ),
    ]
