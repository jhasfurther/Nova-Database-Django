from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from .models import Equipment, Calibration
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

class CalibrationAdmin(admin.TabularInline):
    model = Calibration

class EquipmentAdmin(ImportExportModelAdmin):
    list_display = (
    'inventory_tag',
    'equipment_type',
    'status',
    'description',
    'assignee',
    'calibration_date',
    'due_date',
    'calibrated_by',
    'location',
    'calibration_frequency'
    )

    search_fields = ('inventory_tag',
    'equipment_type',
    'inventory_number',
    'status',
    'manufacturer',
    'description',
    'assignee',
    'calibration_date',
    'due_date')

    list_filter = (
    'equipment_type',
    ('due_date', DateRangeFilter),
    'status',
    'calibrated_by',
    )
    fields = [
        ('equipment_type', 'inventory_number'),
        'inventory_tag',
        'manufacturer',
        'description',
        ('model_number', 'serial_number'),
        'condition_as_recieved',
        ('calibration_date', 'due_date', 'calibration_frequency'),
        'status',
        'introduction_to_service_form',
        'out_of_service_form',
	    'location',
	    'assignee',
	    'calibrated_by',
    ]
    readonly_fields = ('due_date','inventory_tag')
    inlines = [
        CalibrationAdmin,
    ]

admin.site.register(Equipment, EquipmentAdmin)

class EquipmentResource(resources.ModelResource):

    class Meta:
            model = Equipment
            split_tag = Field()
            def dehydrate_split_tag(self, equipment):
                return '%s-%s' % (equipment.equipment_type, equipment.inventory_number)
            fields = (  'inventory_tag',
                        'manufacturer',
                        'description',
                        'model_number',
                        'serial_number',
                        'condition_as_recieved',
                        'calibration_date',
                        'due_date',
                        'calibration_frequency',
                        'status',
                        'location',
                        'assignee',
                        'calibrated_by',
                    )
admin.site.site_url = "/inventory"
