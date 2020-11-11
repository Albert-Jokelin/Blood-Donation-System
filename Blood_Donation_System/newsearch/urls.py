from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index),
    path('details/<int:hospital_id>/', views.details),

]
