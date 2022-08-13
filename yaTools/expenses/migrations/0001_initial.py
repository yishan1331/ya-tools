# Generated by Django 3.2.6 on 2022-08-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30, verbose_name='項目')),
                ('category', models.IntegerField(choices=[(0, '未分類'), (1, '飲食'), (2, '衣服'), (3, '交通'), (4, '教育'), (5, '娛樂'), (99, '其它')], default=0, verbose_name='支出類別')),
                ('amount', models.IntegerField(default=0, verbose_name='支出金額')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30, verbose_name='項目')),
                ('category', models.IntegerField(choices=[(0, '未分類'), (1, '薪水'), (2, '獎金'), (3, '回饋'), (4, '交易'), (5, '股息'), (6, '投資'), (7, '租金'), (99, '其它')], default=0, verbose_name='收入類別')),
                ('amount', models.IntegerField(default=0, verbose_name='收入金額')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]