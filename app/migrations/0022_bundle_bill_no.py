# Generated by Django 5.0.6 on 2024-06-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_packing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='bill_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]