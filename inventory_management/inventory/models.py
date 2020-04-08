from django.db import models


# Create your models here.

class Device(models.Model):  # name of the table

    type = models.CharField (max_length=100, blank=False)  # name of the column
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in the few days')
    )

    status = models.CharField(max_length=100,choices=choices, default='SOLD') #available SOLD ,Restocking
    issues = models.CharField(max_length=100,default='No issues')


    class Meta:
        abstract = True

    def __str__(self):
        return 'type :{0} price:{1}'.format(self.type,self.price)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device) :
    pass





