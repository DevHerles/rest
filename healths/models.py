from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

OPTION_YES = 'SI',
OPTION_NO = 'NO'
options = ((OPTION_YES, 'SI'),(OPTION_NO, 'NO'))


class TypeOfResponse(models.TextChoices):
  YES = ('SI', 'SI')
  NO = ('NO', 'NO')

class Health(models.Model):

  class HealthObjects(models.Manager):
    def get_queryset(self):
      return super().get_queryset().filter(fit=False)

  q1 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q2 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q3 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q4 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q5 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q6 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q7 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q8 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q9 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q10 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q11 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q12 = models.CharField(max_length=2, choices=TypeOfResponse.choices, default=TypeOfResponse.NO)
  q12_detail = models.CharField(max_length=200)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="healths")
  fit = models.BooleanField(default=False)
  created_at = models.DateTimeField(default=timezone.now)
  objects = models.Manager() # default manager
  postobjects = HealthObjects() # custom manager

  class Meta:
    ordering = ('-created_at',)
  
  def __str__(self):
    return self.q1