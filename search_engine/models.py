from django.db import models

# Create your models here.
class PlateRequest(models.Model):
    plate=models.CharField(verbose_name="validator_name", max_length=50)
    vehicle_id=models.CharField(verbose_name="vehicle_id",max_length=80)
    user_id=models.CharField(verbose_name="user_id",max_length=80)

    class Meta: 
        ordering=['-vehicle_id']

    def __str__(self):
        return self.plate
 
