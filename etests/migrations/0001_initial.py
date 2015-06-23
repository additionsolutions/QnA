# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=200, null=True, blank=True)),
                ('SrNo', models.CharField(max_length=100)),
                ('mark', models.IntegerField()),
                ('url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preamble', models.CharField(max_length=200, null=True, blank=True)),
                ('test_question', models.CharField(max_length=500)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('category', models.ForeignKey(to='etests.Category', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=100)),
                ('testname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('no_ans', models.IntegerField(default=1)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('submit_flag', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='TestSetLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('srno', models.IntegerField()),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='etests.TestQuestion', null=True)),
                ('testset', models.ForeignKey(to='etests.TestSet', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='t_question',
            field=models.ForeignKey(to='etests.TestQuestion', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='etests.TestSetLine', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterUniqueTogether(
            name='testsetline',
            unique_together=set([('srno', 'testset')]),
        ),
        migrations.AlterUniqueTogether(
            name='option',
            unique_together=set([('t_question', 'SrNo')]),
        ),
    ]
