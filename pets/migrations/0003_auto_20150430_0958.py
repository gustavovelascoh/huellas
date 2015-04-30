# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20150417_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='genre',
            field=models.CharField(max_length=16, choices=[('None', 'Desconocido'), ('M', 'Macho'), ('F', 'Hembra')], default=('None', 'Desconocido')),
        ),
        migrations.AddField(
            model_name='report',
            name='reporter_name',
            field=models.CharField(max_length=32, default='Anonymous'),
        ),
    ]
