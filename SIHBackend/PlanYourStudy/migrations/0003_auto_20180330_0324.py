# Generated by Django 2.0.3 on 2018-03-30 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlanYourStudy', '0002_auto_20180329_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Location',
            new_name='Address',
        ),
    ]
