#this is where the data will sit to be serilizaed and called to for the view rendering
#from rest_framework import serializers
from inventory.models import Equipment
from rest_framework import serializers

class EquipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    inventory_tag = serializers.CharField()
    calibration_date = serializers.DateField()
    due_date = serializers.DateField()
    calibration_frequency = serializers.IntegerField()
    status = serializers.CharField()
    # Location_in_Lab = serializers.CharField()
    intro_pdf = serializers.FileField(use_url=True)

    def create(self, validated_data):
        return Equipment.objects.create(**validated_data)
