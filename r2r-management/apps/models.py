from django.db import models
from django.utils.translation import gettext_lazy as _  # Add this import


class PropertyArea(models.Model):
    area_name = models.CharField(_("Area Name"), max_length=255, null=False)
    area_description = models.CharField(
        _("Area Description"), max_length=255, null=True
    )

    def __str__(self):
        return f"{self.area_name}"

    class Meta:
        verbose_name = _("Property Area")
        verbose_name_plural = _("Property Area")
        db_table = "property_area"


class BusinessUnit(models.Model):
    unit_number = models.CharField(_("Unit Number"), max_length=100)
    unit_name = models.CharField(_("Unit Name"), max_length=100)
    unit_rental = models.IntegerField(_("Unit Rental"))
    unit_address = models.CharField(_("Unit Address"), max_length=255, null=True)

    area = models.ForeignKey(
        PropertyArea, null=True, on_delete=models.CASCADE, verbose_name=_("Area")
    )

    def __str__(self):
        return f"{self.unit_name} - {self.unit_number}"

    class Meta:
        verbose_name = _("Business Unit")
        verbose_name_plural = _("Business Units")
        db_table = "business_unit"


class UnitFileAttachment(models.Model):
    file_name = models.CharField(_("File Name"), max_length=255)
    file_path = models.FileField(_("File Path"))

    business_unit = models.ForeignKey(
        BusinessUnit, on_delete=models.CASCADE, verbose_name=_("Business Unit")
    )

    def __str__(self):
        return f"{self.file_name}"

    class Meta:
        verbose_name = _("Unit Attachment")
        verbose_name_plural = _("Unit Attachments")
        db_table = "unit_attachment"


class RoomDetails(models.Model):
    room_name = models.CharField(_("Room Name"), max_length=100)
    best_case_rental = models.IntegerField(_("Best Case Rental"))
    worst_case_rental = models.IntegerField(_("Worst Case Rental"))
    actual_rental = models.IntegerField(_("Actual Rental"), null=True)
    is_rental = models.BooleanField(_("Is Rented"), default=False)

    business_unit = models.ForeignKey(
        BusinessUnit,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Business Unit"),
    )

    def __str__(self):
        return f"{self.room_name} - {self.business_unit}"

    class Meta:
        verbose_name = _("Room Detail")
        verbose_name_plural = _("Room Details")
        db_table = "room_details"


class RoomPhoto(models.Model):
    photo_name = models.CharField(_("Photo Name"), max_length=255, null=True)
    photo_path = models.ImageField(_("Photo Path"))

    room = models.ForeignKey(
        RoomDetails, on_delete=models.CASCADE, null=True, verbose_name=_("Room")
    )

    def __str__(self):
        return f"{self.photo_name} - {self.room}"

    class Meta:
        verbose_name = _("Room Photo")
        verbose_name_plural = _("Room Photos")
        db_table = "room_photos"
