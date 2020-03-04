from .views import login, sample_api
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/', login),
    path('sampleapi/', sample_api)
]
