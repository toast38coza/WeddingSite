# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_bridalpartyperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='coming_to_wedding',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guest',
            name='notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guest',
            name='vegetarian',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
