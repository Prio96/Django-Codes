from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField(primary_key=True)
    father_name=models.CharField(max_length=30)
    address=models.TextField()
    
    def __str__(self):
        return f"{self.name}({self.roll})"

    