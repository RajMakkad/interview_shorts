# Generated by Django 4.2.1 on 2023-07-16 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0003_short_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='short',
            name='branch',
        ),
    ]
