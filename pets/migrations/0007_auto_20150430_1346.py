# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_auto_20150430_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='mod_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 18, 45, 57, 886255, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 18, 46, 8, 721569, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(default='NA', blank=True, max_length=32),
        ),
    ]
