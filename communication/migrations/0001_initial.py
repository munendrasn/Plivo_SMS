# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendSMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_number', models.CharField(max_length=30)),
                ('from_number', models.CharField(max_length=30)),
                ('sms_sid', models.CharField(default=b'', max_length=34, blank=True)),
                ('account_sid', models.CharField(default=b'', max_length=34, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(null=True, blank=True)),
                ('delivered_at', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(default=b'', max_length=20, blank=True)),
                ('body', models.TextField(default=b'', max_length=140)),
            ],
        ),
    ]
