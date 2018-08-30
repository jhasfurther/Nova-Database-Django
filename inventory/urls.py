from django.urls import path
from . import views
urlpatterns = [
  path('',views.EquipmentTable , name = 'equipment_list'),
]
