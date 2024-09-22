from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def AddPost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            print(form.cleaned_data)
            form.save()
            return redirect("AddPost")
    else:
        form=PostForm()
    return render(request,'add_post.html',{'form':form})
@login_required
def EditPost(request,id):
    post=Post.objects.get(pk=id)
    form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.instance.author=request.user
            print(form.cleaned_data)
            form.save()
            return redirect("HomePage")
    return render(request,'add_post.html',{'form':form})
@login_required
def DeletePost(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect("HomePage")