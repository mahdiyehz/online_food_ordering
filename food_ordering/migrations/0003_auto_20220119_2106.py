# Generated by Django 3.2.9 on 2022-01-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering', '0002_auto_20220119_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
