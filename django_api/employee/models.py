from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
  
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE) 
    def __str__(self) -> str:
        return self.name
