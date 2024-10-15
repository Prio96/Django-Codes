from django.shortcuts import render
from new_post.models import NewPost
from categories.models import Category
def home(request,category_slug=None):
    post=NewPost.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        post=NewPost.objects.filter(category=category)
    category=Category.objects.all()
    return render(request,"home.html",{'posts':post,'categories':category})