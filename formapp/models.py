from django.db import models

# Create your models here.
class formtable(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    salary=models.IntegerField()
    modile=models.IntegerField()
    emanil=models.EmailField()    
