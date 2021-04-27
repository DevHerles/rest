from django.contrib import admin
from . import models

@admin.register(models.Health)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('id', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q12_detail', 'fit', 'created_at', 'owner')
  prepopulated_fields={'q12_detail': ('q1', 'q2'),}

#  admin.site.register(models.Health)