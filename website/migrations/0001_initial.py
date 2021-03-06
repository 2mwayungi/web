# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-10 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=website.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('publish', models.DateTimeField()),
                ('draft', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
