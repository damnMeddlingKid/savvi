# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20150522_1256'),
        ('users', '0002_auto_20150522_1151'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
