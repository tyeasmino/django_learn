# Generated by Django 4.0.1 on 2022-03-02 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_release_date'),
        ('account', '0012_alter_user_detail_user_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='user_course',
            field=models.CharField(default='no', max_length=100, null=True),
        ),
    ]
