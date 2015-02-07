# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_auto_20150207_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='guest_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
