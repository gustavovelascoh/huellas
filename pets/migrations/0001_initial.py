# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('animal', models.CharField(max_length=32)),
                ('breed', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=32)),
                ('zone', models.CharField(max_length=32, choices=[('None', 'Sin zona'), ('N', 'Norte'), ('S', 'Sur'), ('C', 'Centro'), ('E', 'Este/Oriente'), ('O', 'Oeste/Occidente')])),
                ('n_hood', models.CharField(max_length=32)),
                ('comment', models.TextField()),
                ('type', models.CharField(max_length=16, choices=[('0', 'Perdido'), ('1', 'Encontrado'), ('2', 'Visto')])),
            ],
        ),
        migrations.CreateModel(
            name='ReportImages',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('report_id', models.ForeignKey(to='pets.Report')),
            ],
        ),
    ]
