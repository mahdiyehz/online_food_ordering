# Generated by Django 3.2.9 on 2022-01-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealcategory',
            name='name',
            field=models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner'), ('DRINKS', 'Drinks'), ('APPETIZER', 'Appetizer'), ('DESSERT', 'Dessert')], max_length=10),
        ),
    ]