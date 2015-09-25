# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0008_auto_20150514_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='event_date',
            field=models.DateTimeField(default='2015-01-01 00:00:00'),
        ),
        migrations.AddField(
            model_name='report',
            name='reporter_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(max_length=32, choices=[('0', 'Activo'), ('10', 'Cerrado')], default=0),
        ),
    ]
