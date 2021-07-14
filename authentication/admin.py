from django.contrib import admin
from django.contrib.auth.models import Group
from authentication.models import Profile, Address


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_id', 'name', 'type', 'approved')
    list_filter = ('type', 'approved')


class AdressAdmin(admin.ModelAdmin):
    list_display = ('line1', 'line2', 'city', 'country', 'contactno', 'email')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address, AdressAdmin)
admin.site.site_header = 'Frymn Pharmacy '
admin.site.site_title = 'Dashboard'
admin.site.index_title = 'Frymn Pharmacy'
admin.site.unregister(Group)
