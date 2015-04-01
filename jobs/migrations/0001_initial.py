# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(height_field=b'height', upload_to=b'upload/jobs/images/%Y/%m/%d/', width_field=b'width', max_length=255, verbose_name='Image')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('width', models.PositiveIntegerField(default=0, verbose_name='Width', blank=True)),
                ('height', models.PositiveIntegerField(default=0, verbose_name='Height', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('uploaded', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='job',
            field=models.ForeignKey(related_name='jobs', to='jobs.Job'),
            preserve_default=True,
        ),
    ]
