# Generated by Django 4.0.1 on 2022-02-05 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
