from django.contrib import admin
from .models import ReceiveEnties, ReceiveDetail

# Register your models here.


class ReceiveEntiesAdmin(admin.ModelAdmin):
    pass


class ReceiveDetailAdmin(admin.ModelAdmin):
    pass


admin.site.register(ReceiveEnties, ReceiveEntiesAdmin)
admin.site.register(ReceiveDetail, ReceiveDetailAdmin)
