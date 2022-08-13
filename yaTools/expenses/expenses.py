from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.forms.models import model_to_dict
from .models import Expense, ExpenseCategory, Income

# Create your views here.


# 支出類別列表
class ExpenseCategoryList(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    ordering = ['id']  # 正向排序
    paginate_by = 10    # 每頁顯示幾筆

    template_name = 'expenses/keeping.html'

    def __init__(self):
        # 預設支出類別選項
        self.default_trans_values = {
            'Breakfast': _('Breakfast'),  # 早餐
            'Lunch': _('Lunch'),  # 午餐
            'Dinner': _('Dinner'),  # 晚餐
            'Drinks': _('Drinks'),  # 飲料
            'Liquor': _('Liquor'),  # 酒類
            'Traffic': _('Traffic'),  # 交通
            'Shopping': _('Shopping'),  # 購物
            'Entertainment': _('Entertainment'),  # 娛樂
            'Groceries': _('Groceries'),  # 日用品
            'Medical': _('Medical'),  # 醫療
            'Social': _('Social'),  # 社交
            'Gift': _('Gift'),  # 禮物
            'Other': _('Other'),  # 其它
        }

    context_object_name = 'expensecategorylist'

    # def get_queryset(self):
    #     queryset = super().get_queryset().values_list("name", "name_CH", "image")
    #     print(queryset)
    #     print(type(queryset))
    #     trans_values = {}
    #     # for i in queryset:
    #     #     print(i)
    #     #     newi = model_to_dict(i)
    #     #     print(newi)
    #     #     trans_values[newi.name] = _(newi.name)
    #     print(trans_values)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # queryset = self.get_queryset()
        print(self.default_trans_values)
        context['default_trans_values'] = self.default_trans_values
        return context

# 新增支出紀錄


class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = '__all__'                  # 在表單上顯示*所有*欄位
    template_name = 'form.html'         # 指定使用 form.html 這個頁面範本

    def get_success_url(self):
        return reverse('expense_list')  # 新增成功返回支出紀錄列表頁面
