# Generated by Django 4.0.1 on 2022-05-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_delete_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semester_01',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester_02',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester_03',
            field=models.IntegerField(),
        ),
    ]