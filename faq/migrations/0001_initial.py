# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('description', models.TextField()),
                ('wedding', models.ForeignKey(to='website.Wedding')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
