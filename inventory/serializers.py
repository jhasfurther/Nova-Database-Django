#this is where the data will sit to be serilizaed and called to for the view rendering
#from rest_framework import serializers
from inventory.models import Equipment
from rest_framework import serializers

class InventoryEquipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    Inventory_Tag = serializers.CharField()
    Calibration_Date = serializers.DateField()
    Due_Date = serializers.DateField()
    Calibration_Frequency = serializers.IntegerField()
    Current_Status = serializers.CharField()
    Location_in_Lab = serializers.CharField()
    pdf_of_introduction_to_inventory = serializers.FileField()
    pdf_of_calibration_1 = serializers.FileField()
