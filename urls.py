from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('calibrations/', include('calibrations.urls')),
    paht('inventory/',include('inventory.urls')),
]
