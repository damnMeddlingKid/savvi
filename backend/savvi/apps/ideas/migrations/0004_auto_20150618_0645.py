# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20150522_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 6, 45, 55, 640036, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
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
