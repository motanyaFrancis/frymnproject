from django.contrib import admin
from authentication.models import Profile, Address


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'approved')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
