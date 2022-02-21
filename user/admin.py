from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","message")
admin.site.register(contact,contactAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display=("name","dob","mobile","email","passwd","address","myfile")
admin.site.register(profile,profileAdmin)

class bookingAdmin(admin.ModelAdmin):
    list_display=("tour","trip","name","dob","contact","email","vechile","pas","message")
admin.site.register(booking,bookingAdmin)