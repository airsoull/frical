# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='job',
            field=models.ForeignKey(related_name='images', to='jobs.Job'),
            preserve_default=True,
        ),
    ]
