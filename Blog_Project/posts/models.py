from django.db import models
from author.models import Author
from categories.models import Category
# Create your models here.
#title,content,category,author
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(default=None)
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title