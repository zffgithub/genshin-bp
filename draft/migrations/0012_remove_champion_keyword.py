# Generated by Django 3.0.4 on 2021-01-28 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0011_draft_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='keyword',
        ),
    ]
