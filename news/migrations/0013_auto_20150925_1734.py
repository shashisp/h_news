# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20150925_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hn_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
