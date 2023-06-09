# Generated by Django 4.2.1 on 2023-06-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='school',
            name='principal',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='school',
            name='year_founded',
            field=models.IntegerField(blank=True),
        ),
    ]
