from django.db import models
from model_utils.models import TimeStampedModel


class Tipper(TimeStampedModel):
    class Model(models.TextChoices):
        BELAZ = 'belaz'
        KOMATSU = 'komatsu'

    board_number = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, choices=Model.choices)
    max_load_capacity = models.IntegerField(default=0)
    current_weight = models.IntegerField(default=0)

    @property
    def overload(self):
        return round((self.current_weight / self.max_load_capacity) * 100 - 100) if self.current_weight and \
                                                                                    self.current_weight > \
                                                                                    self.max_load_capacity else None
