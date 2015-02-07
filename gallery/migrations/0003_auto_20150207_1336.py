# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150207_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=datetime.date(2015, 2, 7), editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(help_text=b'The name of the gallery', max_length=100),
        ),
    ]
