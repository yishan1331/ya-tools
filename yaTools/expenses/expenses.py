from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django.core import serializers
import json
from .models import Expense, ExpenseCategory, Income

# Create your views here.


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


# 支出類別列表
class ExpenseCategoryList(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    ordering = ['id']  # 正向排序
    # paginate_by = 10    # 每頁顯示幾筆

    template_name = 'expenses/list.html'

    def __init__(self):
        # 預設支出類別選項
        self.default_trans_values = {
            '早餐': _('早餐'),  # Breakfast
            '午餐': _('午餐'),  # Lunch
            '晚餐': _('晚餐'),  # Dinner
            '飲料': _('飲料'),  # Drinks
            '酒類': _('酒類'),  # Liquor
            '交通': _('交通'),  # Traffic
            '購物': _('購物'),  # Shopping
            '娛樂': _('娛樂'),  # Entertainment
            '日用品': _('日用品'),  # Groceries
            '醫療': _('醫療'),  # Medical
            '社交': _('社交'),  # Social
            '禮物': _('禮物'),  # Gift
            '寵物': _('寵物'),  # Pet
            '其他': _('其他'),  # Other
        }

    context_object_name = 'expensecategorylist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset().values(
            "name", "name_CH", "image")
        print('queryset', queryset)

        # trans_values = {i['name']: _(i['name_CH']) for i in queryset}
        # print('trans_values:', trans_values)
        # context['default_trans_values'] = trans_values
        return context


class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    ordering = ['-date']  # 正向排序
    # paginate_by = 10    # 每頁顯示幾筆

    template_name = 'expenses/list.html'

    context_object_name = 'expenselist'

    def get_queryset(self):
        category = {}
        category_options = []
        for i in json.loads(serializers.serialize(
            "json", ExpenseCategory.objects.all(), fields=(
                "id", "name", "name_CH", "image"))):
            category[i['pk']] = i['fields']
            category_options.append({
                'text': i['fields']['name'],
                'text_CH': i['fields']['name_CH'],
                'value': i['fields']['name'],
                'image': i['fields']['image']
            })

        # https://stackoverflow.com/questions/38471260/django-filtering-by-user-id-in-class-based-listview
        # queryset = [i['fields'] for i in json.loads(serializers.serialize(
        #     "json", super().get_queryset().filter(user=self.request.user).select_related('category')))]
        queryset = json.loads(serializers.serialize(
            "json", Expense.objects.select_related('category').filter(user=self.request.user)))
        expense = []
        for i in queryset:
            c = i['fields']['category']
            expense.append(
                {**i['fields'], **{'category_name': category[c]['name'], 'category_name_CH': category[c]['name_CH']}})
        return {
            "result": expense,
            "category": category,
            "category_options": category_options
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# 新增支出紀錄


# class ExpenseCreate(LoginRequiredMixin, CreateView):
#     model = Expense
#     fields = '__all__'                  # 在表單上顯示*所有*欄位
#     template_name = 'form.html'         # 指定使用 form.html 這個頁面範本

#     def get_success_url(self):
#         return reverse('expense_list')  # 新增成功返回支出紀錄列表頁面
def expenseCreate(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            try:
                print('form', form)
                # form.save()
                # model = form.instance
                return redirect('book-list')
            except:
                pass
    else:
        form = ExpenseForm()
    return render(request, 'book-create.html', {'form': form})
