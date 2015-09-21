# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hn_id', models.IntegerField()),
                ('url', models.URLField()),
                ('hn_url', models.URLField()),
                ('posted_on', models.DateTimeField(null=True)),
                ('up_votes', models.IntegerField()),
                ('comments', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_read', models.NullBooleanField(default=False)),
                ('is_deleted', models.NullBooleanField(default=False)),
                ('article', models.ForeignKey(to='news.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
