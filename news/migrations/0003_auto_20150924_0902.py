# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='posted_on',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
