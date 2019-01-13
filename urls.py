from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calibrations/', include('calibrations.urls')),
    path('inventory/',include('inventory.urls')),
]
