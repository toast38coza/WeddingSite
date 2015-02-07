# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150207_1324'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='wedding',
            field=models.ForeignKey(default=None, to='website.Wedding'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='gallery',
            field=models.ForeignKey(default=0, to='gallery.Gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='wedding',
            field=models.ForeignKey(default=0, to='website.Wedding'),
            preserve_default=False,
        ),
    ]
