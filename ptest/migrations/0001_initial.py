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
                ('answer', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('srno', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('marksalloted', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=100)),
                ('testsetname', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('submit_flag', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='groups', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='TestSetLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('srno', models.IntegerField()),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('testset', models.ForeignKey(to='ptest.TestSet', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AddField(
            model_name='testquestion',
            name='testsetline',
            field=models.ForeignKey(to='ptest.TestSetLine', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='answer',
            name='testquestion',
            field=models.ForeignKey(to='ptest.TestQuestion', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(related_name='user', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='testsetline',
            unique_together=set([('srno', 'testset')]),
        ),
        migrations.AlterUniqueTogether(
            name='testquestion',
            unique_together=set([('srno', 'testsetline')]),
        ),
    ]
