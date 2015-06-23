# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('father_name', models.CharField(default=b'-Not mentioned-', max_length=20)),
                ('mother_name', models.CharField(default=b'-Not mentioned-', max_length=20)),
                ('website', models.URLField(blank=True)),
                ('mobile', models.PositiveIntegerField(default=0)),
                ('picture', models.ImageField(default=b'no_image.png', upload_to=b'profile_images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
