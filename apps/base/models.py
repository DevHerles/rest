from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField('Activo', default=True)
    created_date = models.DateField(
        'Fecha de creación',
        auto_now=False,
        auto_now_add=True,
    )
    modified_date = models.DateField('Fecha de modificación',
                                     auto_now=True,
                                     auto_now_add=False)
    deleted_date = models.DateField('Fecha de eliminación',
                                    auto_now=True,
                                    auto_now_add=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'
