# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=300)),
                ('upvote_count', models.IntegerField()),
                ('downvote_count', models.IntegerField()),
                ('author', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(to='ideas.Idea'),
        ),
    ]
