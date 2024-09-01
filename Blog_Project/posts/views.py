from django.shortcuts import render,redirect
from .forms import PostForm
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