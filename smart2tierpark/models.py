from django.db import models
from .Platform import Platform
import datetime
class Log(models.Model):
    veh_num=models.ForeignKey('auth.User')
    platform_number=models.TextField()
    timein=models.DateTimeField()
    timeout=models.DateTimeField()
    totaltime=models.TextField()
    totalcost=models.TextField()


    
    
    
    
