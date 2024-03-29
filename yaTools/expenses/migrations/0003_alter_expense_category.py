# Generated by Django 3.2.6 on 2022-08-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20220811_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'fa-burger'), ('Lunch', 'fa-bowl-rice'), ('Dinner', 'fa-utensils'), ('Drinks', 'fa-mug-saucer'), ('Liquor', 'fa-martini-glass-citrus'), ('Traffic', 'fa-bus'), ('Shopping', 'fa-shopify'), ('Entertainment', 'fa-gamepad'), ('Groceries', 'fa-cart-shopping'), ('Medical', 'fa-hospital'), ('Social', 'fa-people-group'), ('Gift', 'fa-gift'), ('Other', 'fa-border-all')], default='fa-burger', max_length=30, verbose_name='支出類別'),
        ),
    ]
