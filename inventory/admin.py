from django.contrib import admin

from .models import Equipment, Calibration

class CalibrationAdmin(admin.TabularInline):
    model = Calibration

class EquipmentAdmin(admin.ModelAdmin):
    fields = [
        ('equipment_type', 'inventory_number'),
        'inventory_tag',
        'manufacturer',
        'description',
        ('model_number', 'serial_number'),
        'condition_as_recieved',
        ('calibration_date', 'due_date', 'calibration_frequency'),
        'status',
        'intro_pdf',
	    'location',
	    'assignee',
	    'calibrated_by',
    ]
    readonly_fields = ('due_date','inventory_tag')
    inlines = [
        CalibrationAdmin,
    ]

admin.site.register(Equipment, EquipmentAdmin)
