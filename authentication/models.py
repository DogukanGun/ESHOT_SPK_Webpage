from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    username=models.CharField(max_length=30,verbose_name="username")
    name=models.CharField(max_length=30,default="noName",verbose_name="name")
    password=models.CharField(max_length=20,verbose_name="password")
    user_type = models.CharField(max_length=20,verbose_name="user_type")
    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-password']