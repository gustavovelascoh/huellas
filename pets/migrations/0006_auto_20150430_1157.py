# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_auto_20150430_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='genre',
            field=models.CharField(default='None', max_length=32, choices=[('None', 'Desconocido'), ('M', 'Macho'), ('F', 'Hembra')]),
        ),
        migrations.AlterField(
            model_name='report',
            name='type',
            field=models.CharField(max_length=32, choices=[('0', 'Perdido'), ('1', 'Encontrado'), ('2', 'Visto')]),
        ),
    ]
