from django.db import models
from django.conf import settings
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords


class WorkType(BaseModel):
    code = models.CharField(max_length=255,
                            unique=True,
                            blank=False,
                            null=False)
    description = models.CharField(max_length=255, blank=False, null=False)

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def __history_user(self, value):
        self.changed_by = value

    class Meta:
        ordering = ('description', )

    def __str__(self):
        return f'{self.code} - {self.description}'
