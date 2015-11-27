# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_post_publish_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_at',
            field=models.DateTimeField(verbose_name='publish at'),
        ),
    ]
