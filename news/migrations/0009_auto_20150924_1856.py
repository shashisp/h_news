# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_delete_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='article',
        ),
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]
