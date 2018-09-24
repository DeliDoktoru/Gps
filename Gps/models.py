from django.db import models

class Employer(models.Model):
    name=models.CharField(max_length=200)
    mail=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    token=models.CharField(max_length=200)
    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"
class Employee(models.Model):
    name=models.CharField(max_length=200)
    employer=models.ForeignKey(Employer, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
class Coordination(models.Model):
    lat=models.FloatField()
    lon=models.FloatField()
    date=models.DateTimeField()
    employe=models.ForeignKey(Employee, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Coordination"
        verbose_name_plural = "Coordinations"