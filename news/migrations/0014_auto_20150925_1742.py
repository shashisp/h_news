# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20150925_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='posted_on',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
