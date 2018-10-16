from django.contrib import admin

from .models import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    fields = (
        ('equipment_type', 'inventory_number'),
        'inventory_tag',
        'manufacturer',
        'description',
        ('model_number', 'serial_number'),
        'condition_as_recieved',
        ('calibration_date', 'due_date', 'calibration_frequency'),
        'status',
        'pdf_of_introduction_to_inventory',
	    'location',
	    'assignee',
	    'calibrated_by',
    )
    readonly_fields = ('due_date','inventory_tag')

admin.site.register(Equipment, EquipmentAdmin)
