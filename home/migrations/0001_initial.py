# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('caption', models.CharField(default=b'', max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('sequence', models.IntegerField()),
            ],
            options={
                'ordering': ['sequence'],
                'managed': True,
            },
        ),
    ]
