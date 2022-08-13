from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Expense(models.Model):
    # 預設支出類別選項
    # fa-solid
    CATE_CHOICES = (
        ('Breakfast', "fa-burger"),  # 早餐
        ('Lunch', "fa-bowl-rice"),  # 午餐
        ('Dinner', "fa-utensils"),  # 晚餐
        ('Drinks', "fa-mug-saucer"),  # 飲料
        ('Liquor', "fa-martini-glass-citrus"),  # 酒類
        ('Traffic', "fa-bus"),  # 交通
        ('Shopping', "fa-shopify"),  # 購物
        ('Entertainment', "fa-gamepad"),  # 娛樂
        ('Groceries', "fa-cart-shopping"),  # 日用品
        ('Medical', "fa-hospital"),  # 醫療
        ('Social', "fa-people-group"),  # 社交
        ('Gift', "fa-gift"),  # 禮物
        ('Other', "fa-border-all"),  # 其它
    )
    # 欄位定義
    item = models.CharField('項目', max_length=30)
    category = models.CharField(
        '支出類別', default='fa-burger', max_length=30, choices=CATE_CHOICES)
    amount = models.IntegerField('支出金額', default=0)
    remarks = models.CharField('備註', default=None, max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class ExpenseCategory(models.Model):
    # 欄位定義
    name = models.CharField('類別名稱', max_length=30)
    name_CH = models.CharField('中文類別名稱', max_length=30)
    image = models.CharField('類別圖案', max_length=30)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    # 收入類別選項
    CATE_CHOICES = (
        (0, "未分類"),
        (1, "薪水"),
        (2, "獎金"),
        (3, "回饋"),
        (4, "交易"),
        (5, "股息"),
        (6, "投資"),
        (7, "租金"),
        (99, "其它"),
    )
    # 欄位定義
    item = models.CharField('項目', max_length=30)
    category = models.IntegerField('收入類別', default=0, choices=CATE_CHOICES)
    amount = models.IntegerField('收入金額', default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
