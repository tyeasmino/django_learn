# Generated by Django 4.0.1 on 2022-03-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_id_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='study_center',
            field=models.CharField(max_length=3),
        ),
    ]
