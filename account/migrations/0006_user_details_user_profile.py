# Generated by Django 4.0.1 on 2022-02-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_user_details_user_study_center_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='user_Profile',
            field=models.ImageField(default='', null=True, upload_to='user/profile'),
        ),
    ]
