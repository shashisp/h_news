# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20150924_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='hn_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='hn_url',
            field=models.URLField(blank=True),
        ),
    ]
