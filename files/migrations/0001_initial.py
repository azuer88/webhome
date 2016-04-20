# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=30)),
                ('filename', models.FileField(upload_to=b'files/')),
                ('filetype', models.SmallIntegerField(default=1, choices=[(1, b'Image'), (2, b'Video'), (3, b'Audio'), (4, b'Other')])),
            ],
        ),
    ]
