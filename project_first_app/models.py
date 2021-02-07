from django.db import models


# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    vehicles = models.ManyToManyField('Vehicle', through='Ownership')


class Licence(models.Model):
    TYPES = (
        ('A', 'Motocycle'),
        ('B', 'Car'),
        ('C', 'Truck'),
        ('D', 'Bus')
    )
    licence_id = models.IntegerField()
    licence_date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=50)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    buy_date = models.DateField(blank=True, null=True)
    sell_date = models.DateField(blank=True, null=True)


