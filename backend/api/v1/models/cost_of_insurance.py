import datetime

from tortoise import fields, models


class CostOfInsurance(models.Model):
    """
    Модель стоимости страховки
    """

    id = fields.UUIDField(pk=True, index=True)
    actual_date = fields.DateField(default=datetime.datetime.now)
    cargo = fields.CharField(min_length=3, max_length=50, indexable=True)
    rate = fields.FloatField()

    class Meta:
        unique_together = [("actual_date", "cargo")]
