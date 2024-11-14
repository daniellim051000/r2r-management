from apps.models import (
    BusinessUnit,
    RoomDetails,
    RoomPhoto,
    UnitFileAttachment,
    PropertyArea,
)
from expenses.models import UnitExpenses

from django.contrib import admin
from django.utils.safestring import mark_safe


# Room Photo Inline (to be used in RoomDetails)
class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1
    fields = ("photo_name", "photo_path")


# Unit File Attachment Inline
class UnitFileAttachmentInline(admin.TabularInline):
    model = UnitFileAttachment
    extra = 1
    fields = ("file_name", "file_path")


# Room Details Inline
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


# Expenses Inline
class ExpensesInline(admin.TabularInline):
    model = UnitExpenses
    extra = 1
    fields = ("name", "description", "amount", "attachment")


# Business Unit Admin
class BusinessUnitAdmin(admin.ModelAdmin):
    list_display = ("unit_number", "unit_name", "unit_rental", "area")
    search_fields = ("unit_number", "unit_name")
    list_filter = ("unit_rental", "area")

    inlines = [UnitFileAttachmentInline, RoomDetailsInline, ExpensesInline]


# Room Details Admin (new)
@admin.register(RoomDetails)
class RoomDetailsAdmin(admin.ModelAdmin):
    list_display = (
        "room_name",
        "business_unit",
        "best_case_rental",
        "actual_rental",
        "is_rental",
    )
    list_filter = ("is_rental", "business_unit")
    search_fields = ("room_name", "business_unit__unit_name")
    inlines = [RoomPhotoInline]


# Room Photo Admin (new)
@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = ("photo_name", "room", "photo_preview")
    list_filter = ("room__business_unit",)
    search_fields = ("photo_name", "room__room_name")

    def photo_preview(self, obj):
        if obj.photo_path:
            return mark_safe(f'<img src="{obj.photo_path.url}" width="100" />')
        return "No photo"

    photo_preview.short_description = "Photo Preview"


# Register remaining models
admin.site.register(BusinessUnit, BusinessUnitAdmin)
admin.site.register(PropertyArea)
