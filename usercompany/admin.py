from django.contrib import admin
from usercompany.models import CompanyStock


# Register your models here.
class CompanyStockAdmin(admin.ModelAdmin):
    list_display = ('batch_no', 'profile', 'medicine', 'quantity', 'price', 'mfd_date', 'exp_date')
    list_filter = ('batch_no', 'exp_date', 'medicine')
    search_fields = ('batch_no', 'medicine')


admin.site.register(CompanyStock, CompanyStockAdmin)
