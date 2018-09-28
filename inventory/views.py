#from django.http import JsonResponse
#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import Template
#import json
#from django.core import serializers

#def EquipmentList(request):
#    Equipment_As_Table = Equipment.objects.all()
#    return render(request, 'lists.html')
#def JsonView(request):
 #   Equipment_as_json = serializers.serialize('json',Equipment.objects.all(), fields = ('id',))
  #  return JsonResponse(Equipment_as_json,safe=False)


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
