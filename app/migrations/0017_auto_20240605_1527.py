# Generated by Django 3.2.10 on 2024-06-05 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_bundle_disable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='disable',
        ),
        migrations.DeleteModel(
            name='Selected',
        ),
    ]