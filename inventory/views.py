from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Equipment
from .serializers import EquipmentSerializer
from django.http import HttpResponse

def index(request):
    return render(request, 'lists.html')

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return response.Response(serializer.data)
