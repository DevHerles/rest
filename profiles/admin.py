from django.contrib import admin
from .models import Profile, Setting, Theme, Layout, Config, Bar

admin.site.register(Profile)
admin.site.register(Setting)
admin.site.register(Theme)
admin.site.register(Layout)
admin.site.register(Config)
admin.site.register(Bar)

# Register your models here.
