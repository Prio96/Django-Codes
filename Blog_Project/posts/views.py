from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def AddPost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("AddPost")
    else:
        form=PostForm()
    return render(request,'add_post.html',{'form':form})
def EditPost(request,id):
    post=Post.objects.get(pk=id)
    form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("HomePage")
    return render(request,'add_post.html',{'form':form})

def DeletePost(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect("HomePage")