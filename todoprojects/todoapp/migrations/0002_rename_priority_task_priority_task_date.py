# Generated by Django 4.1 on 2022-10-08 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Priority',
            new_name='priority',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
