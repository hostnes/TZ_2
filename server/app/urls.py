from django.urls import path, include

from .views import rates

urlpatterns = [
    path('rates', rates, name='rates'),
]