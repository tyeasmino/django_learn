# Generated by Django 4.0.1 on 2022-04-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('study_center', models.CharField(max_length=3)),
                ('default_pass', models.CharField(default='DCSA', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
