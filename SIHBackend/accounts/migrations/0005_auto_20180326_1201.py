# Generated by Django 2.0.3 on 2018-03-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180326_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonregistration',
            name='user',
        ),
        migrations.AddField(
            model_name='commonregistration',
            name='User_email',
            field=models.EmailField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='commonregistration',
            name='User_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]