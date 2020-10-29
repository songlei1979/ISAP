from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class ServiceLevel(models.Model):
    servicelevelID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=90, null=False, blank=False)
    serviceRate = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(10)], null=True, blank=False)


class Location(models.Model):
    locationID = models.AutoField(primary_key=True)
    suburb = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)

class EquipmentType(models.Model):
    equipmentTypeID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=90, null=False, blank=False)
    leaserate = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(15)], null=False, blank=False)

class Division(models.Model):
    divisionID = models.AutoField(primary_key=True)
    serviceLevel = models.ForeignKey(ServiceLevel, on_delete=models.CASCADE, to_field='servicelevelID', null=False, blank=False)
    description = models.CharField(max_length=90, null=False, blank=False)

class DIVAndLOC(models.Model):
    divAndLocID = models.AutoField(primary_key=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, to_field='divisionID', null=False,
                                     blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, to_field='locationID', null=False,
                                     blank=False)

class Building(models.Model):
    buildingID = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, to_field='locationID', null=False,
                                     blank=False)
    buildingName = models.CharField(max_length=20, null=False, blank=False)
    streetAddress = models.CharField(max_length=30, null=False, blank=False)
    supportFactor = models.FloatField(validators=[MaxValueValidator(200), MinValueValidator(20)], null=False, blank=False)


class Desk(models.Model):
    deskID = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, to_field='buildingID', null=False,
                                     blank=False)
    place = models.CharField(max_length=500, null=False, blank=False)
    status = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    Status = models.CharField(max_length=6, choices=status, null=False, blank=False)


class Equipment(models.Model):
    equipmentID = models.AutoField(primary_key=True)
    equipmentType = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, to_field='equipmentTypeID', null=False, blank=False)
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE, to_field='deskID', null=False, blank=False)
    status = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    )
    Status = models.CharField(max_length=11, choices=status, null=False, blank=False)

class Employee(models.Model):
    employeeID = models.AutoField(primary_key=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, to_field='divisionID', null=False, blank=False)
    divisionDescription = models.CharField(max_length=90, null=False, blank=False)
    lastname = models.CharField(max_length=30, null=False, blank=False)
    firstname = models.CharField(max_length=30, null=False, blank=False)
    emailAddress = models.CharField(max_length=20, null=False, blank=False)
    phoneNumber = models.CharField(max_length=15, null=False, blank=False)

class EmpAndDesk(models.Model):
    empAndDeskID = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='employeeID', null=False, blank=False)
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE, to_field='deskID', null=False, blank=False)
