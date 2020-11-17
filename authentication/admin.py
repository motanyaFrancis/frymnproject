from django.contrib import admin
from authentication.models import Profile, Address


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_id', 'name', 'type', 'approved')
    list_filter = ('type', 'approved')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)

