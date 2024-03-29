# Generated by Django 3.2.6 on 2022-08-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='類別名稱')),
                ('image', models.CharField(max_length=30, verbose_name='類別圖案')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='remarks',
            field=models.CharField(default=None, max_length=50, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('fa-burger', '早餐'), ('fa-bowl-rice', '午餐'), ('fa-utensils', '晚餐'), ('fa-mug-saucer', '飲料'), ('fa-martini-glass-citrus', '酒類'), ('fa-bus', '交通'), ('fa-shopify', '購物'), ('fa-gamepad', '娛樂'), ('fa-cart-shopping', '日用品'), ('fa-hospital', '醫療'), ('fa-people-group', '社交'), ('fa-gift', '禮物'), ('fa-border-all', '其它')], default='fa-burger', max_length=30, verbose_name='支出類別'),
        ),
    ]
