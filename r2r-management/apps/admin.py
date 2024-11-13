from apps.models import (
    BusinessUnit,
    RoomDetails,
    RoomPhoto,
    UnitFileAttachment,
    PropertyArea,
)
from expenses.models import UnitExpenses

from django.contrib import admin


class UnitFileAttachmentInline(admin.TabularInline):
    model = UnitFileAttachment
    extra = 1
    fields = ("file_name", "file_path")


class RoomDetailsInline(admin.TabularInline):
    model = RoomDetails
    extra = 1
    fields = (
        "room_name",
        "best_case_rental",
        "worst_case_rental",
        "actual_rental",
        "is_rental",
    )


class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1
    fields = ("photo_name", "photo_path")


class ExpensesInline(admin.TabularInline):
    model = UnitExpenses
    extra = 1
    fields = ("name", "description", "amount", "attachment")


class BusinessUnitAdmin(admin.ModelAdmin):
    list_display = ("unit_number", "unit_name", "unit_rental", "area")
    search_fields = ("unit_number", "unit_name")
    list_filter = ("unit_rental", "area")

    inlines = [UnitFileAttachmentInline, RoomDetailsInline, ExpensesInline]


# Register the models
admin.site.register(BusinessUnit, BusinessUnitAdmin)
admin.site.register(PropertyArea)
