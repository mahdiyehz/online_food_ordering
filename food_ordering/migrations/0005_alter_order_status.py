# Generated by Django 3.2.9 on 2022-01-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering', '0004_auto_20220119_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Ordered'), ('2', 'Recorded'), ('3', 'Sent'), ('4', 'Delivered')], max_length=10),
        ),
    ]