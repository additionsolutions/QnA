# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='etests.TestSetLine', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
