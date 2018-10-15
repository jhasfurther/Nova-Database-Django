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
        'pdf_of_introduction_to_inventory',
        'pdf_of_calibration_1',
        'pdf_of_calibration_2',
        'pdf_of_calibration_3',
        'pdf_of_calibration_4',
        'pdf_of_calibration_5',
	    'Location_In_Lab',
	    'Who_Is_It_Assigned_To',
	    'Calibrated_By',
    )
    readonly_fields = ('Due_Date','Inventory_Tag')

admin.site.register(Equipment, EquipmentAdmin)
