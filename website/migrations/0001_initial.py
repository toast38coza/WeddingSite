# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouplePhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to=b'landing-page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_title', models.CharField(max_length=100, blank=True)),
                ('meta_description', models.CharField(max_length=100, blank=True)),
                ('headline', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('tagline', models.CharField(max_length=100, blank=True)),
                ('background_image', models.ImageField(upload_to=b'landing-page', blank=True)),
                ('enabled', models.BooleanField(default=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('intro', models.TextField()),
                ('headline', models.CharField(max_length=100)),
                ('partner_one', models.CharField(max_length=100)),
                ('partner_two', models.CharField(max_length=100)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeddingCeremonyVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('extra_info', models.TextField(blank=True)),
                ('start_datetime', models.DateTimeField()),
                ('address', models.TextField()),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('wedding', models.ForeignKey(to='website.Wedding')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeddingReceptionVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('extra_info', models.TextField(blank=True)),
                ('start_datetime', models.DateTimeField()),
                ('address', models.TextField()),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('wedding', models.ForeignKey(to='website.Wedding')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='section',
            name='wedding',
            field=models.ForeignKey(to='website.Wedding'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='couplephotos',
            name='wedding',
            field=models.ForeignKey(to='website.Wedding'),
            preserve_default=True,
        ),
    ]
