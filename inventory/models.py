from django.db import models
import datetime
from dateutil.relativedelta import relativedelta

class Equipment (models.Model):

    OFFICE_CHOICES = (
    ('NOVA Reno','NOVA Reno'),
    ('NOVA Las Vegas','NOVA Las Vegas'),
    ('NOVA SoCal','NOVA SoCal'),
)

    EQUIPMENT_TYPES = (
        ('TL','Tool'),
        ('BA','Balance and Scales'),
        ('SV','Sieve'),
        ('CM','Compaction Mold'),
        ('CS','Cleanness Sieve'),
        ('SC','Soundness Sieve'),
        ('MA','Machine'),
        ('SS','Slump Set'),
        ('SST','Slump Set Thermometer'),
        ('DI', 'Dial Indicator'),
        ('NDT', 'Non Destructive Testing'),
)
    CONDITIONS = (
        ('New','New'),
        ('Used','Used'),
        ('Good','Good'),
    )
    CALIBRATORS = (
        ('National', 'National'),
        ('ADTEK','ADTEK'),
        ('In House', 'In House'),
        ('Manufacturer','Manufacturer'),
        ('Other','Other')
    )
    STATUSES = (
        ('On Lease','On Lease'),
        ('Missing','Missing'),
        ('Need to be Repaired','Need to be Repaired'),
        ('In Service','In Service'),
        ('Out of Service','Out of Service'),
    )
    inventory_tag = models.CharField(default=None, max_length=20)
    equipment_type = models.CharField(max_length=256, default=None, choices=EQUIPMENT_TYPES)
    inventory_number = models.CharField(max_length=200,default=None)
#    Office = models.CharField(default=None, null=True, blank=True, max_length=20, choices=OFFICE_CHOICES)
    description = models.CharField(default=None, max_length=200,blank=True,null=True)
    manufacturer =  models.CharField(blank=True, max_length=200,default=None)
    model_number = models.CharField(blank=True, null=True, max_length=200,default=None)
    serial_number = models.CharField(blank=True, null=True, max_length=200,default=None)
    condition_as_recieved = models.CharField(blank=True, null=True, max_length=10, default='New', choices=CONDITIONS)
    calibration_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    calibration_frequency = models.IntegerField(blank=True, null=True, help_text='months')
    calibrated_by = models.CharField(blank=True, null=True, max_length=200,default=None, choices=CALIBRATORS)
    status = models.CharField(blank=True, null=True, max_length=200,default=None, choices=STATUSES)
    location = models.CharField(blank=True, null=True, max_length=200,default=None)
    introduction_to_service_form = models.FileField(blank=True, null=True, default=None)
    out_of_service_form = models.FileField(blank=True, null=True, default=None)
    assignee = models.CharField(blank=True, null=True, max_length=200,default=None)

    class Meta:
        verbose_name_plural = "Equipment"
        unique_together = ('equipment_type', 'inventory_number')

    def save(self, *args, **kwargs):
        if self.inventory_tag:
            self.equipment_type = self.inventory_tag.split('-')[0]
            self.inventory_number = self.inventory_tag.split('-')[1]
        elif self.equipment_type and self.inventory_number:
            self.inventory_tag = self.equipment_type + '-' + str(self.inventory_number)
        if self.calibration_date and self.calibration_frequency:
            self.due_date = self.calibration_date + relativedelta(months=+self.calibration_frequency)
        super(Equipment, self).save(*args, **kwargs)

    def __str__(self):
        return self.inventory_tag

class Calibration (models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_calibrated = models.DateField()
    pdf = models.FileField(blank=True, null=True, default=None)
    calibrator = models.CharField(max_length=256, default=None)

    def __str__(self):
        return str(self.equipment.inventory_tag) + " - " + str(self.date_calibrated)
