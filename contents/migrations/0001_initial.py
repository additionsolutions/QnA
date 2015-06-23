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
            name='AcademicDuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now=True)),
                ('data', models.TextField(blank=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('video', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academicduration', models.ForeignKey(to='contents.AcademicDuration')),
                ('content', models.ForeignKey(to='contents.Content')),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentAcademicDuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current', models.ForeignKey(to='contents.AcademicDuration')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='contenttype',
            field=models.ForeignKey(to='contents.ContentType', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='content',
            name='createdby',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='groups',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
