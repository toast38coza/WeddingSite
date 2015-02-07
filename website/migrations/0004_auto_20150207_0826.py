# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_bridalpartymember'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.PositiveIntegerField(default=100, help_text=b'Order in which you would like to display sections'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bridalpartymember',
            name='role_detail',
            field=models.CharField(help_text=b"For example, 'Mother', 'Father', 'Maid of Honor' or 'Best Man'", max_length=100, null=True, blank=True),
        ),
    ]
