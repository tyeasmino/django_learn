# Generated by Django 4.0.1 on 2022-01-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyCenter',
            fields=[
                ('studyCenter_code', models.IntegerField(primary_key=True, serialize=False)),
                ('studyCenter_name', models.CharField(max_length=100)),
                ('studyCenter_location', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
