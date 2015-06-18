# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20150522_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='downvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='idea',
            name='upvote_count',
            field=models.IntegerField(default=0),
        ),
    ]
