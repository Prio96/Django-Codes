from django.db import models
from author.models import Author
# Create your models here.
#name,about
class Profile(models.Model):
    name=models.CharField(max_length=50)
    about=models.TextField(default=None)
    author=models.OneToOneField(Author,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.name