from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import NewUser
# Create your models here.


class Bar(models.Model):
    class BarsPosition(models.TextChoices):
        LEFT = 'left', _('Left')
        RIGHT = 'right', _('Right')
        BELOW = 'below', _('Below')
        TOP = 'top', _('Top')

    display = models.BooleanField(default=True)
    folded = models.BooleanField(default=True)
    position = models.CharField(max_length=10,
                                choices=BarsPosition.choices,
                                default=BarsPosition.LEFT)
    style = models.CharField(max_length=10)

    def __str__(self):
        return self.position

class Config(models.Model):
    scroll = models.CharField(max_length=10, default='content')
    navbar = models.ForeignKey(Bar,
                               on_delete=models.CASCADE,
                               null=False,
                               related_name='config_navbar')
    toolbar = models.ForeignKey(Bar,
                                on_delete=models.CASCADE,
                                null=False,
                                related_name='config_toolbar')
    footer = models.ForeignKey(Bar,
                               on_delete=models.CASCADE,
                               null=False,
                               related_name='config_footer')
    mode = models.CharField(max_length=20, default='fullwidth')

    def __str__(self):
        return self.navbar.position


class Layout(models.Model):
    style = models.CharField(max_length=10, default='style1')
    config = models.ForeignKey(Config, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.style


class Theme(models.Model):
    main = models.CharField(max_length=15, default='default', null=False)
    navbar = models.CharField(max_length=15, default='defaultDark', null=False)
    toolbar = models.CharField(max_length=15, default='default', null=False)
    footer = models.CharField(max_length=15, default='default', null=False)

    def __str__(self):
        return self.main


class Setting(models.Model):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE, null=False)
    custom_scrollbars = models.BooleanField(default=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.theme.main

    class Meta:
        verbose_name = 'Congifuración'
        verbose_name_plural = 'Configuraciones'


class Profile(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=False)
    settings = models.ForeignKey(Setting,
                                 on_delete=models.CASCADE,
                                 null=False)

    def __str__(self):
        return self.user.user_name
