# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20150430_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='genre',
            field=models.CharField(default='None', choices=[(None, 'Desconocido'), ('M', 'Macho'), ('F', 'Hembra')], max_length=32),
        ),
        migrations.AlterField(
            model_name='report',
            name='zone',
            field=models.CharField(choices=[(None, 'Sin zona'), ('N', 'Norte'), ('S', 'Sur'), ('C', 'Centro'), ('E', 'Este/Oriente'), ('O', 'Oeste/Occidente')], max_length=32),
        ),
    ]
