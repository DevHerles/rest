from django.db import models
from django.conf import settings
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
from apps.organs.models import Organ
from apps.work_types.models import WorkType
from apps.organic_units.models import OrganicUnit


class Partner(BaseModel):
    partner_type = models.CharField(max_length=255, blank=True, null=True)
    doc_number = models.CharField(max_length=255, blank=True, null=True)
    doc_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=9, blank=True, null=True)
    organ = models.ForeignKey(Organ,
                              on_delete=models.CASCADE,
                              related_name='partners',
                              blank=True,
                              null=True)
    organic_unit = models.ForeignKey(OrganicUnit,
                                     on_delete=models.CASCADE,
                                     related_name='partners',
                                     blank=True,
                                     null=True)
    functional_team = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    work_type = models.ForeignKey(WorkType,
                                  on_delete=models.CASCADE,
                                  related_name='partners',
                                  blank=True,
                                  null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='partners',
                              blank=True,
                              null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def __history_user(self, value):
        self.changed_by = value

    class Meta:
        ordering = ('doc_type', 'doc_number')

    def __str__(self):
        return f'{self.name} {self.first_name} {self.last_name}'
