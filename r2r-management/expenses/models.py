from apps.models import BusinessUnit

from django.db import models
from django.utils.translation import gettext_lazy as _  # Add this import


class UnitExpenses(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.CharField(_("Description"), max_length=255)
    amount = models.IntegerField(_("Amount"))
    attachment = models.FileField(_("Attachment"))

    business_unit = models.ForeignKey(
        BusinessUnit, on_delete=models.CASCADE, verbose_name=_("Business Unit")
    )

    class Meta:
        verbose_name = _("Unit Expense")
        verbose_name_plural = _("Unit Expenses")
        db_table = "unit_expenses"
