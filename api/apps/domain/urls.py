from django.contrib import admin
from django.urls import  path

from apps.domain.views.health_views import health

urlpatterns = [
    path('health', health, name='health'),
]
