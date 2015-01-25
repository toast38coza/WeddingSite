# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='headline',
            field=models.CharField(help_text=b"This is what will show as the heading for this section. e.g.: 'Logistics'", max_length=100),
        ),
        migrations.AlterField(
            model_name='section',
            name='tagline',
            field=models.CharField(help_text=b"Put something here if you want to add a little context to the headline. 'Venues, accommodation and things to do'", max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='headline',
            field=models.CharField(help_text=b"The heading to your welcome message. Something like: 'We're getting married' works well", max_length=100),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='intro',
            field=models.TextField(help_text=b'This is the text that shows up as the welcome message'),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='site',
            field=models.ForeignKey(help_text=b"Don't worry about this one ..", to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='weddingceremonyvenue',
            name='address',
            field=models.TextField(help_text=b'What is the address for this venue'),
        ),
        migrations.AlterField(
            model_name='weddingceremonyvenue',
            name='extra_info',
            field=models.TextField(help_text=b'Some extra info about it. Maybe what it looks like, or something cool about the place', blank=True),
        ),
        migrations.AlterField(
            model_name='weddingceremonyvenue',
            name='latitude',
            field=models.CharField(help_text=b'The latitude (you can get this off google maps) - it will be used to render the map on this page', max_length=100),
        ),
        migrations.AlterField(
            model_name='weddingceremonyvenue',
            name='longitude',
            field=models.CharField(help_text=b'The longitude (you can get this off google maps) - it will be used to render the map on this page', max_length=100),
        ),
        migrations.AlterField(
            model_name='weddingceremonyvenue',
            name='start_datetime',
            field=models.DateTimeField(help_text=b'When does the ceremony start?'),
        ),
        migrations.AlterField(
            model_name='weddingceremonyvenue',
            name='title',
            field=models.CharField(help_text=b'The name of the venue', max_length=100),
        ),
    ]
