from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField('Activo', default=True)
    created_date = models.DateField(
        'Fecha de creación',
        auto_now=False,
        auto_now_add=True,
    )
    modified_date = models.DateField('Fecha de modificación',
                                     auto_now=True,
                                     auto_now_add=False)
    deleted_date = models.DateField('Fecha de eliminacón',
                                    auto_now=True,
                                    auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'
