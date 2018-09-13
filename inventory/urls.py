#from django.urls import path
#from . import views
#urlpatterns = [
#  path(r'^json/',views.JsonView),
#  path('',views.EquipmentList),
#]

from django.conf.urls import url, include
from rest_framework import routers
from inventory import views

router = routers.DefaultRouter()
router.register(r'inventory', views.EquipmentViewSet)

urlpatterns = [
    url('/api', include(router.urls)),
    url('', views.index, name='inventory'),
]
