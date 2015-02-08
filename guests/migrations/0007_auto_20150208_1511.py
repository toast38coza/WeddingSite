# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0006_remove_guest_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bridalpartyperson',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='bridalpartyperson',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bridalpartyperson',
            name='wedding',
        ),
        migrations.DeleteModel(
            name='BridalPartyPerson',
        ),
        migrations.AddField(
            model_name='guest',
            name='gender',
            field=models.CharField(default=b'Female', max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guest',
            name='is_family',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
