# Generated by Django 4.1 on 2022-09-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mobile_verified',
            field=models.BooleanField(default=False),
        ),
    ]
