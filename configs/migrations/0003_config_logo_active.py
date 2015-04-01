# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0002_auto_20150401_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='logo_active',
            field=models.BooleanField(default=True, verbose_name='Logo Active'),
            preserve_default=True,
        ),
    ]
