# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20150925_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='up_votes',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
