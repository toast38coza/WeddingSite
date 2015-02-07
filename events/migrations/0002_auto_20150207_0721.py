# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.TextField(help_text=b'Address where this event will be held', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(upload_to=b'events', blank=True),
        ),
    ]
