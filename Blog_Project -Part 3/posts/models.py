from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
# Create your models here.
#title,content,category,author
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(default=None)
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    email=models.EmailField()
    name=models.CharField(max_length=30)
    body=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.name}"


    
    

