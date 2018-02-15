# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0015_auto_20180215_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='tag',
        ),
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(default=b'1.jpeg', upload_to=b'. /static/img', blank=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='P_tag',
            field=models.ManyToManyField(to='socialapp.Tags', blank=True),
        ),
    ]
