from django.contrib import admin
from .models import (
    CorpFormulaVCST,
    ProductFormulaVCST,
    ProductTypeFormulaVCST,
    UmFormulaVCST,
    PdGrdFormulaVCST,
    WhouseFormulaVCST,
    EmployeeVCST,
    CoorVCST,
    GlrefVCST
)

# Register your models here.


class CorpFormulaVCSTAdmin(admin.ModelAdmin):
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


class ProductTypeFormulaVCSTAdmin(admin.ModelAdmin):
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


class ProductFormulaVCSTAdmin(admin.ModelAdmin):
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


class UmFormulaVCSTAdmin(admin.ModelAdmin):
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


class PdGrdFormulaVCSTAdmin(admin.ModelAdmin):
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


class WhouseFormulaVCSTAdmin(admin.ModelAdmin):
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


class EmployeeVCSTAdmin(admin.ModelAdmin):
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


class CoorVCSTAdmin(admin.ModelAdmin):
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


class GlrefVCSTAdmin(admin.ModelAdmin):
    list_display = (
        "FCCODE",
        "FCREFNO",
        "FTDATETIME",
        "FTLASTUPD",
    )
    pass


admin.site.register(CorpFormulaVCST, CorpFormulaVCSTAdmin)
admin.site.register(ProductTypeFormulaVCST, ProductTypeFormulaVCSTAdmin)
admin.site.register(ProductFormulaVCST, ProductFormulaVCSTAdmin)
admin.site.register(UmFormulaVCST, UmFormulaVCSTAdmin)
admin.site.register(PdGrdFormulaVCST, PdGrdFormulaVCSTAdmin)
admin.site.register(WhouseFormulaVCST, WhouseFormulaVCSTAdmin)
admin.site.register(EmployeeVCST, EmployeeVCSTAdmin)
admin.site.register(CoorVCST, CoorVCSTAdmin)
admin.site.register(GlrefVCST, GlrefVCSTAdmin)
