# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0003_config_logo_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='logo',
            field=models.ImageField(upload_to=b'upload/config/logo/%Y/%m/%d/', width_field=b'width', height_field=b'height', blank=True, null=True, verbose_name='Logo'),
            preserve_default=True,
        ),
    ]
