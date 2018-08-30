from django.db import models

class Calibrations (models.Model):
    Type_of_Calibration = models.CharField(max_length=50, default=None)
    pdf_of_Instructions = models.FileField(default=None)
    pdf_of_Calibration_Sheet = models.FileField(default=None)

    def __str__(self):
        return self.Type_of_Calibration

