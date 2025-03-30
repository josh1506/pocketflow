from django.contrib import admin

from .models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "amount",
        "date",
    )
    search_fields = (
        "title",
        "description",
    )
    list_filter = (
        "category",
        "created_at",
        "updated_at",
        "deleted_at",
    )