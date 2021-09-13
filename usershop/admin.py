from django.contrib import admin
from usershop.models import ShopStock


# Register your models here.
class ShopStockAdmin(admin.ModelAdmin):
    list_display = ('profile','medicine', 'quantity', 'price', 'exp_date')
    list_filter = ('exp_date', 'medicine')
    # search_fields = ('medicine', 'profile')


admin.site.register(ShopStock, ShopStockAdmin)
