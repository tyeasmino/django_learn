# Generated by Django 4.0.1 on 2022-02-07 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_release_date'),
        ('StudyCenter', '0010_remove_coursesemseter_semester_course_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesemseter',
            name='semester_course_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
