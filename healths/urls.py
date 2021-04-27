from django.urls import path
from django.views.generic import TemplateView

app_name = "healths"

urlpatterns = [
  path('', TemplateView.as_view(template_name="healths/index.html"))
]