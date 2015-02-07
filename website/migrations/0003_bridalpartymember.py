# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150125_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='BridalPartyMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=100, choices=[(b'Bride', b'Bride'), (b'Groom', b'Groom'), (b'Mom', b'Mom'), (b'Dad', b'Dad'), (b'Bridesmaid', b'Bridesmaid'), (b'Groomsman', b'Groomsman')])),
                ('side', models.CharField(max_length=100, choices=[(b'His', b'His'), (b'Hers', b'Hers')])),
                ('role_detail', models.CharField(help_text=b"For example, 'Maid of Honor' or 'Best Man'", max_length=100, null=True, blank=True)),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('picture', models.ImageField(upload_to=b'bridalparty', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
