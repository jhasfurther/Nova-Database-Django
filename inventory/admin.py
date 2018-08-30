from django.contrib import admin

from .models import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    fields = (
        ('Equipment_List', 'Inventory_Number'),
        'Inventory_Tag',
        'Manufacturer',
        'Description_of_Item',
        'Model_Number',
        'Serial_Number',
        'Condition_as_recieved',
        'Calibration_Date',
        'Due_Date',
        'Calibration_Frequency',
        'Current_Status',
        'pdf_1',
	'pdf_2',
        'pdf_3',
        'pdf_4',
        'pdf_5',
        'pdf_6',
	'Location_In_Lab'
    )
    readonly_fields = ('Due_Date','Inventory_Tag')

admin.site.register(Equipment, EquipmentAdmin)
