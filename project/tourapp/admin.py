from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

class TravelBookAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','email','phone','destination','seats')
    search_fields = ('email','destination')
    list_filter=('destination','email')

admin.site.register(Pakage)
admin.site.register(TravelBook,TravelBookAdmin)
admin.site.register(VendorRegister)

admin.site.register(Profile)