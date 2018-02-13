# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CateUsr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categ', models.ForeignKey(to='socialapp.Category')),
                ('user', models.ForeignKey(to='socialapp.Users')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_body', models.CharField(max_length=255)),
                ('c_user', models.ForeignKey(to='socialapp.Users')),
                ('id_post', models.ForeignKey(to='socialapp.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('R_body', models.CharField(max_length=255)),
                ('R_user', models.ForeignKey(to='socialapp.Users')),
                ('post_id', models.ForeignKey(to='socialapp.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='unwanted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=50)),
            ],
        ),
    ]
