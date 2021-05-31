from django.db import models
from django.utils import timezone
from apps.base.models import BaseModel


class Setting(BaseModel):
    layout_style = models.CharField(max_length=255, default='layout1')
    layout_config_scroll = models.CharField(max_length=255, default='content')
    layout_config_navbar_position = models.CharField(max_length=255,
                                                     default='left')
    layout_config_navbar_display = models.BooleanField(default=True)
    layout_config_navbar_folded = models.BooleanField(default=False)
    layout_config_toolbar_position = models.CharField(max_length=255,
                                                      default='below')
    layout_config_toolbar_style = models.CharField(max_length=255,
                                                   default='fixed')
    layout_config_toolbar_display = models.BooleanField(default=True)
    layout_config_footer_position = models.CharField(max_length=255,
                                                     default='below')
    layout_config_footer_display = models.BooleanField(default=True)
    layout_config_footer_style = models.CharField(max_length=255,
                                                  default='fixed')
    layout_config_mode = models.CharField(max_length=255, default='fullwidth')
    custom_scrollbars = models.BooleanField(default=True)
    theme_main = models.CharField(max_length=255, default='default')
    theme_navbar = models.CharField(max_length=255, default='defaultDark')
    theme_toolbar = models.CharField(max_length=255, default='default')
    theme_footer = models.CharField(max_length=255, default='default')
    created_at = models.DateTimeField(default=timezone.now)
    objects = models.Manager()  # default manager

    class Meta:
        ordering = ('-created_at', )

    # def __str__(self):
    #     return self.owner.name if self.owner else 'Unknown'
