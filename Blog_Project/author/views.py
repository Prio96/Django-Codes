from django.shortcuts import render,redirect
from .forms import AuthorForm
# Create your views here.
def AddAuthor(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("AddAuthor")
    else:
        form=AuthorForm()
    return render(request,"add_author.html",{'form':form})
