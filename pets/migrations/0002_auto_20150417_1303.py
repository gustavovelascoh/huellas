# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='reportimages',
            name='report_id',
        ),
        migrations.AddField(
            model_name='report',
            name='email',
            field=models.EmailField(max_length=254, default=''),
        ),
        migrations.AddField(
            model_name='report',
            name='phone',
            field=models.CharField(max_length=32, default=''),
        ),
        migrations.DeleteModel(
            name='ReportImages',
        ),
        migrations.AddField(
            model_name='reportimage',
            name='report_id',
            field=models.ForeignKey(to='pets.Report'),
        ),
    ]
