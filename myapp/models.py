from django.db import models

# Create your models here.

class Event(models.Model):
    event_name=models.CharField(max_length=30)
    event_catagory=models.CharField(max_length=30)
    event_image=models.ImageField(blank=True, null=True)
    event_startdate=models.CharField(max_length=30)
    event_enddate=models.CharField(max_length=30)
    def __str__(self):
        return str(self.event_name)

class Contestant(models.Model):
    contestant_id=models.CharField(max_length=30, unique=True)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    contestant_name=models.CharField(max_length=30)
    contestant_image=models.ImageField(blank=True, null=True)
    contestant_age=models.CharField(max_length=30)
    contentant_height=models.CharField(max_length=30)


