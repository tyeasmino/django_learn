# Generated by Django 4.0.1 on 2022-02-06 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_release_date'),
        ('StudyCenter', '0004_rename_couser_name_studycenter_s_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studycenter',
            name='s_course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]