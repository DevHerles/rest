from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import NewUser
# Create your models here.


class Bars(models.Model):
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


class Configs(models.Model):
    scroll = models.CharField(max_length=10, default='content')
    navbar = models.ForeignKey(Bars,
                               on_delete=models.CASCADE,
                               null=False,
                               related_name='config_navbar')
    toolbar = models.ForeignKey(Bars,
                                on_delete=models.CASCADE,
                                null=False,
                                related_name='config_toolbar')
    footer = models.ForeignKey(Bars,
                               on_delete=models.CASCADE,
                               null=False,
                               related_name='config_footer')
    mode = models.CharField(max_length=20, default='fullwidth')


class Layouts(models.Model):
    style = models.CharField(max_length=10, default='style1')
    config = models.ForeignKey(Configs, on_delete=models.CASCADE, null=False)


class Themes(models.Model):
    main = models.CharField(max_length=15, default='default', null=False)
    navbar = models.CharField(max_length=15, default='defaultDark', null=False)
    toolbar = models.CharField(max_length=15, default='default', null=False)
    footer = models.CharField(max_length=15, default='default', null=False)


class Settings(models.Model):
    layout = models.ForeignKey(Layouts, on_delete=models.CASCADE, null=False)
    custom_scrollbars = models.BooleanField(default=True)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, null=False)


class Profiles(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=False)
    settings = models.ForeignKey(Settings,
                                 on_delete=models.CASCADE,
                                 null=False)
