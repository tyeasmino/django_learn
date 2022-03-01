# Generated by Django 4.0.1 on 2022-02-09 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_release_date'),
        ('StudyCenter', '0018_coursesemseter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(default='', max_length=100)),
                ('book_unit_no', models.CharField(default='', max_length=30)),
                ('book_unit_name', models.CharField(default='', max_length=100)),
                ('book_unit_page', models.CharField(default='', max_length=10)),
                ('book_course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('book_semester_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudyCenter.semester')),
            ],
        ),
    ]
