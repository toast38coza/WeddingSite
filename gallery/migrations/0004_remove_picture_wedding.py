# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150207_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='wedding',
        ),
    ]
