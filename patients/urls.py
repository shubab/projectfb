from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.patient_list, name='pl'),
    path('patient_detail/<int:id>/', views.patient_detail, name='patient_detail'),
    path('chat/', views.patient_entry, name='patient_ent'),
]

