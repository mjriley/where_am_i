# Generated by Django 3.1.1 on 2020-09-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whereami', '0001_create_user_and_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimagiuser',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
