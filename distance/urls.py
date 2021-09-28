from django.urls import path
from . import views


urlpatterns = [
    path('', views.measure_length, name='measure_length')
]
