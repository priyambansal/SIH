# Generated by Django 2.0.3 on 2018-03-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanYourStudy', '0003_auto_20180330_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Fees',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='category',
            name='InstituteType',
            field=models.CharField(choices=[('Government', 'Government'), ('Private', 'Private')], default='Government', max_length=100),
        ),
    ]
