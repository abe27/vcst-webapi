from django.contrib import admin
from .models import ReceiveEnties

# Register your models here.


class ReceiveEntiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(ReceiveEnties, ReceiveEntiesAdmin)
