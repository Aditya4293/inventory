# Generated by Django 3.2.10 on 2024-06-11 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_packing_total_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='total_weight',
        ),
    ]
