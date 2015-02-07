# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0003_bridalpartymember'),
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BridalPartyPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to=b'picture', blank=True)),
                ('guest', models.ForeignKey(to='guests.Guest')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('wedding', models.ForeignKey(to='website.Wedding')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
