from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    marks=models.FloatField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name