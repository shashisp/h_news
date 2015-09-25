# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20150925_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-posted_on',)},
        ),
        migrations.AddField(
            model_name='article',
            name='rank',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
