from django.db import models
from django.utils import timezone
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
from apps.partners.models import Partner

OPTION_YES = 'SI',
OPTION_NO = 'NO'
options = ((OPTION_YES, 'SI'), (OPTION_NO, 'NO'))


class TypeOfResponse(models.TextChoices):
    YES = ('SI', 'SI')
    NO = ('NO', 'NO')


class Health(BaseModel):
    class HealthObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(fit=False)

    q1 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q2 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q3 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q4 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q5 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q6 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q7 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q8 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q9 = models.CharField(max_length=2,
                          choices=TypeOfResponse.choices,
                          default=TypeOfResponse.NO)
    q10 = models.CharField(max_length=2,
                           choices=TypeOfResponse.choices,
                           default=TypeOfResponse.NO)
    q11 = models.CharField(max_length=2,
                           choices=TypeOfResponse.choices,
                           default=TypeOfResponse.NO)
    q12 = models.CharField(max_length=2,
                           choices=TypeOfResponse.choices,
                           default=TypeOfResponse.NO)
    q12_detail = models.CharField(max_length=200, blank=True, null=True)
    partner_id = models.ForeignKey(Partner,
                                   on_delete=models.CASCADE,
                                   related_name="healths",
                                   null=True)
    fit = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    objects = models.Manager()  # default manager
    postobjects = HealthObjects()  # custom manager

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def __history_user(self, value):
        self.changed_by = value

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.partner_id.name} {self.partner_id.first_name} {self.partner_id.last_name}'
