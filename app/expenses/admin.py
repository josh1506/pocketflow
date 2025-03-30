from django.contrib import admin

from .models import Expenses


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "amount",
        "category",
    )
    search_fields = (
        "id",
        "title",
    )
    list_filter = (
        "category",
        "created_at",
        "updated_at",
        "deleted_at",
    )
