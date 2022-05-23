# Generated by Django 4.0.3 on 2022-05-11 08:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='create_date',
            field=models.DateField(default=datetime.date(2022, 5, 11)),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.district')),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.group')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.region')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.region'),
        ),
    ]