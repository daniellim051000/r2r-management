from django.db import models


class BusinessUnit(models.Model):
    unit_number = models.CharField(max_length=100)
    unit_name = models.CharField(max_length=100)
    unit_rental = models.IntegerField()
    unit_address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.unit_number} - {self.unit_name}"

    class Meta:
        verbose_name = "Business Unit"
        verbose_name_plural = "Business Units"
        db_table = "business_unit"


class UnitFileAttachment(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.FileField()

    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Unit Attachment"
        verbose_name_plural = "Unit Attachments"
        db_table = "unit_attachment"


class RoomDetails(models.Model):
    room_name = models.CharField(max_length=100)
    best_case_rental = models.IntegerField()
    worst_case_rental = models.IntegerField()
    actual_rental = models.IntegerField(null=True)
    is_rental = models.BooleanField(default=False)

    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Room Detail"
        verbose_name_plural = "Room Details"
        db_table = "room_details"


class RoomPhoto(models.Model):
    photo_name = models.CharField(max_length=255)
    photo_path = models.ImageField()

    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Room Photo"
        verbose_name_plural = "Room Photos"
        db_table = "room_photos"
