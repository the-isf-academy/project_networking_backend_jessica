# Generated by Django 5.1.2 on 2024-10-23 00:19

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_palette_tone'),
    ]

    operations = [
        migrations.AddField(
            model_name='palette',
            name='likes',
            field=banjo.models.IntegerField(default=0),
        ),
    ]
