# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='height',
            field=models.PositiveIntegerField(default=0, verbose_name='Height', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='config',
            name='logo',
            field=models.ImageField(height_field=b'height', upload_to=b'upload/config/logo/%Y/%m/%d/', width_field=b'width', null=True, verbose_name='Logo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='config',
            name='width',
            field=models.PositiveIntegerField(default=0, verbose_name='Width', blank=True),
            preserve_default=True,
        ),
    ]
