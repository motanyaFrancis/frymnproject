from django.contrib import admin
from useradmin.models import Medicine


# Register your models here.
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'details')
    search_fields = ('name', 'type')


admin.site.register(Medicine, MedicineAdmin)
