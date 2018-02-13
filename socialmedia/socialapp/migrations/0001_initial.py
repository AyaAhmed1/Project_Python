# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.CharField(max_length=255)),
                ('p_body', models.CharField(max_length=255)),
                ('like', models.IntegerField()),
                ('dislike', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=50)),
                ('cat_name', models.ForeignKey(to='socialapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('is_admin', models.IntegerField()),
                ('is_blocked', models.IntegerField()),
            ],
        ),
    ]
