# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150125_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'The name of the venue', max_length=100)),
                ('start_datetime', models.DateTimeField(help_text=b'When does the event start?')),
                ('address', models.TextField(help_text=b'Address where this event will be held')),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to=b'events')),
                ('wedding', models.ForeignKey(to='website.Wedding')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
