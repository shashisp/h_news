# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20150925_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hn_id',
            field=models.IntegerField(default=None, blank=True),
        ),
    ]
