# Generated by Django 3.2.10 on 2024-06-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
