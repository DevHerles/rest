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


class Organ(BaseModel):
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


class OrganicUnit(BaseModel):
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


class Partner(BaseModel):
    partner_type = models.CharField(max_length=255)
    doc_number = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=9)
    organ_id = models.ForeignKey(Organ,
                                 on_delete=models.CASCADE,
                                 related_name='partners')
    organic_unit_id = models.ForeignKey(OrganicUnit,
                                        on_delete=models.CASCADE,
                                        related_name='partners')
    functional_team = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    work_type_id = models.ForeignKey(WorkType,
                                     on_delete=models.CASCADE,
                                     related_name='partners')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='partners')
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
