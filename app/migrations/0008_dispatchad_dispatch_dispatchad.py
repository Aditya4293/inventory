# Generated by Django 5.0.6 on 2024-05-28 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_dispatch_bundle_dispatch_grade_dispatch_lot_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatchad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bill_no', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='dispatch',
            name='dispatchad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dispatches', to='app.dispatchad'),
        ),
    ]
