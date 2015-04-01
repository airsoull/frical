# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('site', models.OneToOneField(related_name='config', to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
