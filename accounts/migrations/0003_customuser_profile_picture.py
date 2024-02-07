# Generated by Django 4.2.4 on 2023-10-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default_icon.jpeg', upload_to='static/user/img'),
        ),
    ]