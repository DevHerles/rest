from django.contrib import admin
from .models import Profiles, Settings, Themes, Layouts, Configs, Bars

admin.site.register(Profiles)
admin.site.register(Settings)
admin.site.register(Themes)
admin.site.register(Layouts)
admin.site.register(Configs)
admin.site.register(Bars)

# Register your models here.
