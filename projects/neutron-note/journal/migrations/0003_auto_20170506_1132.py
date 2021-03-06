# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 11:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0002_auto_20170506_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=350)),
                ('sorder', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('sorder',),
            },
        ),
        migrations.RemoveField(
            model_name='entry',
            name='data',
        ),
        migrations.AddField(
            model_name='link',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Entry'),
        ),
        migrations.AddField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
