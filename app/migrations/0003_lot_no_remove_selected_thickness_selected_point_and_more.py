# Generated by Django 5.0.6 on 2024-05-24 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_brand_bundle_customuser_month_packing_party_point_quality_selected_spage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot_no',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='selected',
            name='thickness',
        ),
        migrations.AddField(
            model_name='selected',
            name='point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.point'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='selected',
            name='date',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='selected',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quality'),
        ),
        migrations.AlterField(
            model_name='selected',
            name='weight',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='lott',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lot_no')),
            ],
        ),
        migrations.CreateModel(
            name='lottdataa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=100, unique=True)),
                ('weight', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=100)),
                ('sheet', models.CharField(max_length=20)),
                ('flag', models.CharField(max_length=50)),
                ('total_weight', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=20)),
                ('remarks', models.CharField(max_length=20)),
                ('lot_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lot_no')),
                ('point', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.point')),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quality')),
            ],
        ),
    ]