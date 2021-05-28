from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
import django
import os
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')

django.setup()

GROUPS = ['admin', 'anonymous']
MODELS = ['user']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
