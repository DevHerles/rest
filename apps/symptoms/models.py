from django.db import models
from django.utils import timezone
from django.conf import settings

OPTION_YES = 'SI',
OPTION_NO = 'NO'
options = ((OPTION_YES, 'SI'), (OPTION_NO, 'NO'))


class TypeOfResponse(models.TextChoices):
    YES = ('SI', 'SI')
    NO = ('NO', 'NO')


class Symptom(models.Model):
    class SymptomObjects(models.Manager):
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
    q5_detail = models.CharField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="symptoms")
    fit = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    objects = models.Manager()  # default manager
    postobjects = SymptomObjects()  # custom manager

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.owner.name
