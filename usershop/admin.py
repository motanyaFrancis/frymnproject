from django.contrib import admin
from usershop.models import ShopStock


# Register your models here.
class ShopStockAdmin(admin.ModelAdmin):
    list_display = ('profile','medicine', 'quantity', 'price')


admin.site.register(ShopStock, ShopStockAdmin)
