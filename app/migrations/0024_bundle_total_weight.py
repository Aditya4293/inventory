# Generated by Django 3.2.10 on 2024-06-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_packing_date_packing'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='total_weight',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]