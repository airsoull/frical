# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('body', models.TextField(verbose_name='Body')),
                ('sent', models.DateTimeField(auto_now_add=True, verbose_name='Sent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
