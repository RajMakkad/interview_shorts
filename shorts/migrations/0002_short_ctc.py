# Generated by Django 4.2.1 on 2023-07-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='short',
            name='ctc',
            field=models.TextField(default='50k'),
        ),
    ]
