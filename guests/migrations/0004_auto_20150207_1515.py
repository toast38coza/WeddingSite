# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_auto_20150207_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='partner',
            field=models.ForeignKey(default=None, blank=True, to='guests.Guest', null=True),
        ),
    ]
