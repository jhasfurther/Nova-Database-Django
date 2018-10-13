from django.db import models
import datetime
from dateutil.relativedelta import relativedelta

class Equipment (models.Model):

    Equipment_List = models.CharField(max_length=256, default=None, choices=[('Tool','Tool'),('BA','BA'),('Sieve','Sieve'),('Compaction Mold','Compaction Mold'),('Cleanness Sieve','Cleanness Sieve'),('Soundness Sieve','Soundness Sieve'),('Marshall Aaparatus','Marshall Aparatus'),('Slump Set','Slump Set'),('Slump set thermometer','Slump Set Thermometer')])
    Inventory_Tag = models.CharField(default=None, max_length=20,unique=True)
    Description_of_Item = models.CharField(default=None, max_length=200,blank=True,null=True)
    Inventory_Number = models.CharField(max_length=200,default=None)
    Manufacturer =  models.CharField(max_length=200,default=None)
    Model_Number = models.CharField(max_length=200,default=None)
    Serial_Number = models.CharField(max_length=200,default=None)
    Condition_as_recieved = models.CharField(max_length=10, default='New', null=True, choices=[('New','New'),('Used','Used')])
    Calibration_Date = models.DateField()
    Due_Date = models.DateField()
    Calibration_Frequency = models.IntegerField(help_text='months')
    Calibrated_By = models.CharField(max_length=200,default=None, choices=[('National', 'National'),('ADTEK','ADTEK'),('In House', 'In House'),('Manufacturer','Manufacturer'),('Other','Other')])
    Current_Status = models.CharField(max_length=200,default=None, choices=[('On Lease','On Lease'),('Missing','Missing'),('Need to be Repaired','Need to be Repaired'),('In Service','In Service'),('Out of Service','Out of Service')])
    Location_In_Lab = models.CharField(max_length=200,default=None)
    pdf_of_introduction_to_inventory = models.FileField(blank=True,default=None)
    pdf_of_calibration_1 = models.FileField(blank=True,default=None)
    pdf_of_calibration_2 = models.FileField(blank=True,default=None)
    pdf_of_calibration_3 = models.FileField(blank=True,default=None)
    pdf_of_calibration_4 = models.FileField(blank=True,default=None)
    pdf_of_calibration_5 = models.FileField(blank=True,default=None)
    Who_Is_It_Assigned_To = models.FileField(blank=True,default=None)

    def save(self, *args, **kwargs):
        self.Inventory_Tag = self.Equipment_List + '-' + str(self.Inventory_Number)
        self.Due_Date = self.Calibration_Date + relativedelta(months=+self.Calibration_Frequency)
        super(Equipment, self).save(*args, **kwargs)

    def __str__(self):
        return self.Equipment_List + '-' + str(self.Inventory_Number)
