# Generated by Django 3.2.10 on 2024-06-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_bundle_total_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='packing',
            name='total_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]