from django.contrib import admin
from .models import Order, Type


@admin.register(Type)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("type",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("number", "date_time", "type_order", "completeness")
    list_editable = ("completeness",)
    list_filter = ("type_order",)
    search_fields = ("number",)
