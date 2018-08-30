
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page

from django.shortcuts import render
from inventory.models import Equipment
from inventory.Tables import EquipmentListJson

def EquipmentTable(request):
    Inventory = EquipmentListJson()
    return render(request, "lists.html",locals())
