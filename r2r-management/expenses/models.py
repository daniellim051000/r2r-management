from apps.models import BusinessUnit

from django.db import models


class UnitExpenses(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
    attachment = models.FileField()

    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
