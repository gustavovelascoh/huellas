# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20150430_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='genre',
            field=models.CharField(choices=[('None', 'Desconocido'), ('M', 'Macho'), ('F', 'Hembra')], max_length=16, default='None'),
        ),
    ]
