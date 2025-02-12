# Generated by Django 5.0.6 on 2024-05-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_dispatchad_dispatch_dispatchad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispatch',
            name='dispatchad',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='bill_no',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='bundle',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='packing_name',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='quality',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='sheet',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='sizes',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='thickness',
        ),
        migrations.RemoveField(
            model_name='dispatch',
            name='weight',
        ),
        migrations.AlterField(
            model_name='dispatch',
            name='lot_no',
            field=models.CharField(default='TEMP_DEFAULT', max_length=100),
        ),
        migrations.DeleteModel(
            name='Dispatchad',
        ),
    ]
