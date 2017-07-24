# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-24 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='plannedTrips',
            field=models.ManyToManyField(related_name='users', to='exam_app.Trip'),
        ),
    ]