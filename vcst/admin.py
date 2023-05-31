from django.contrib import admin
from .models import (
    Corp,
    Product,
    ProductType,
    Um,
    PdGrd,
    Whouse,
    Employee,
    Coor,
    Glref,
    Dept,
    Sect
)

# Register your models here.


class CorpAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
    )

    list_filter = [
        # "FCTYPE",
        "FTDATETIME",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
        "FTDATETIME",
        "FTLASTUPD",
    )

    # fieldsets = (
    #     ("Infomation", {
    #         "fields": ("name", "formula_key", "description",),
    #     }),
    #     ("Data Base", {
    #         "fields": ("ip_address", "port", "db_name", "db_user", "db_password",),
    #     }),
    #     (None, {
    #         "fields": ("is_active",),
    #     }),
    # )
    pass


class ProductTypeAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
    )

    list_filter = [
        # "FCTYPE",
        "FTDATETIME",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
        "FTDATETIME",
        "FTLASTUPD",
    )

    # fieldsets = (
    #     ("Infomation", {
    #         "fields": ("name", "formula_key", "description",),
    #     }),
    #     ("Data Base", {
    #         "fields": ("ip_address", "port", "db_name", "db_user", "db_password",),
    #     }),
    #     (None, {
    #         "fields": ("is_active",),
    #     }),
    # )
    pass


class ProductAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCSNAME",
    )

    list_filter = [
        "FCTYPE",
        "FTDATETIME",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCPDGRP",
        "FCTYPE",
        "FCUM",
        "FTDATETIME",
        "FTLASTUPD",
    )

    fieldsets = (
        ("ข้อมูลทั่วไป", {
            "fields": (
                "FCCODE",
                "FCNAME",
                "FCNAME2",
                "FCSNAME",
                "FCSNAME2",),
        }),
        ("รายละเอียดเพิ่มเติม", {
            "fields": (
                "FCCORP",
                "FCTYPE",
                "FCPDGRP",
                "FCUM",),
        }),
    )
    pass


class UmAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
    )

    list_filter = [
        "FTDATETIME",
        "FCCODE",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
        "FTDATETIME",
        "FTLASTUPD",
    )

    # fieldsets = (
    #     ("Infomation", {
    #         "fields": ("name", "formula_key", "description",),
    #     }),
    #     ("Data Base", {
    #         "fields": ("ip_address", "port", "db_name", "db_user", "db_password",),
    #     }),
    #     (None, {
    #         "fields": ("is_active",),
    #     }),
    # )
    pass


class PdGrdAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
    )

    list_filter = [
        "FTDATETIME",
        "FCCODE",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
        "FTDATETIME",
        "FTLASTUPD",
    )

    # fieldsets = (
    #     ("Infomation", {
    #         "fields": ("name", "formula_key", "description",),
    #     }),
    #     ("Data Base", {
    #         "fields": ("ip_address", "port", "db_name", "db_user", "db_password",),
    #     }),
    #     (None, {
    #         "fields": ("is_active",),
    #     }),
    # )
    pass


class WhouseAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
    )

    list_filter = [
        "FTDATETIME",
        "FCCODE",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
        "FTDATETIME",
        "FTLASTUPD",
    )

    # fieldsets = (
    #     ("Infomation", {
    #         "fields": ("name", "formula_key", "description",),
    #     }),
    #     ("Data Base", {
    #         "fields": ("ip_address", "port", "db_name", "db_user", "db_password",),
    #     }),
    #     (None, {
    #         "fields": ("is_active",),
    #     }),
    # )
    pass


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = (
        "FCLOGIN",
        "FCPW",
        "FCRCODE",
    )

    list_filter = [
        "FTDATETIME",
    ]
    list_display = (
        "FCLOGIN",
        "FCPW",
        "FCRCODE",
        "FTDATETIME",
        "FTLASTUPD",
    )
    pass


class CoorAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCSNAME",
        "FCBRANCHNM",
    )

    list_filter = [
        "FTDATETIME",
        "FCCORP",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNO",
        "FCMOO",
        "FCTAMBON",
        "FCAMPHUR",
        "FCPROVINCE",
        "FCZIP",
        "FTLASTUPD",
    )
    pass


class GlrefAdmin(admin.ModelAdmin):
    search_fields = (
        "FCREFNO",
    )
    list_display = (
        "FCCODE",
        "FCREFNO",
        "FTDATETIME",
        "FTLASTUPD",
    )
    pass


class DeptAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
    )

    list_filter = [
        "FTDATETIME",
        "FCCODE",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
        "FTDATETIME",
        "FTLASTUPD",
    )
    pass


class SectAdmin(admin.ModelAdmin):
    search_fields = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
    )

    list_filter = [
        "FTDATETIME",
        "FCDEPT",
    ]
    list_display = (
        "FCCODE",
        "FCNAME",
        "FCNAME2",
        "FTDATETIME",
        "FTLASTUPD",
    )
    pass


admin.site.register(Corp, CorpAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Um, UmAdmin)
admin.site.register(PdGrd, PdGrdAdmin)
admin.site.register(Whouse, WhouseAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Coor, CoorAdmin)
admin.site.register(Glref, GlrefAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Sect, SectAdmin)
