# Generated by Django 3.2.9 on 2022-01-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering', '0003_auto_20220119_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branch',
            name='is_main',
            field=models.BooleanField(verbose_name='main branch'),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
    ]