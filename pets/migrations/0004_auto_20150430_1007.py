# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20150430_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='breed',
            field=models.CharField(default='Criollo', max_length=32),
        ),
        migrations.AlterField(
            model_name='report',
            name='color',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='email',
            field=models.EmailField(default='', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='n_hood',
            field=models.CharField(default='NA', max_length=32),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='phone',
            field=models.CharField(default='', max_length=32, blank=True),
        ),
    ]
