# Generated by Django 2.0.3 on 2018-03-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanYourStudy', '0005_category_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Check',
            field=models.BooleanField(default=False),
        ),
    ]
