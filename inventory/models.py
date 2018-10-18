from django.db import models
import datetime
from dateutil.relativedelta import relativedelta

class Equipment (models.Model):
    EQUIPMENT_TYPES = (
        ('Tool','Tool'),
        ('BA','BA'),
        ('Sieve','Sieve'),
        ('Compaction Mold','Compaction Mold'),
        ('Cleanness Sieve','Cleanness Sieve'),
        ('Soundness Sieve','Soundness Sieve'),
        ('Marshall Aaparatus','Marshall Aparatus'),
        ('Slump Set','Slump Set'),
        ('Slump set thermometer','Slump Set Thermometer')
    )
    CONDITIONS = (
        ('New','New'),
        ('Used','Used')
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
        ('Out of Service','Out of Service')
    )
    equipment_type = models.CharField(max_length=256, default=None, choices=EQUIPMENT_TYPES)
    inventory_tag = models.CharField(default=None, max_length=20)
    inventory_number = models.CharField(max_length=200,default=None)
    description = models.CharField(default=None, max_length=200,blank=True,null=True)
    manufacturer =  models.CharField(max_length=200,default=None)
    model_number = models.CharField(blank=True, null=True, max_length=200,default=None)
    serial_number = models.CharField(blank=True, null=True, max_length=200,default=None)
    condition_as_recieved = models.CharField(blank=True, null=True, max_length=10, default='New', choices=CONDITIONS)
    calibration_date = models.DateField()
    due_date = models.DateField()
    calibration_frequency = models.IntegerField(blank=True, null=True, help_text='months')
    calibrated_by = models.CharField(blank=True, null=True, max_length=200,default=None, choices=CALIBRATORS)
    status = models.CharField(blank=True, null=True, max_length=200,default=None, choices=STATUSES)
    location = models.CharField(blank=True, null=True, max_length=200,default=None)
    intro_pdf = models.FileField(blank=True, null=True, default=None)
    assignee = models.CharField(blank=True, null=True, max_length=200,default=None)

    class Meta:
        verbose_name_plural = "Equipment"
        unique_together = ('equipment_type', 'inventory_number')

    def save(self, *args, **kwargs):
        self.inventory_tag = self.equipment_type + '-' + str(self.inventory_number)
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
