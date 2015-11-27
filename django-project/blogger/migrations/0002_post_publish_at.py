# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_at',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 4, 34, 1, 376242, tzinfo=utc), verbose_name='publish at'),
            preserve_default=False,
        ),
    ]
