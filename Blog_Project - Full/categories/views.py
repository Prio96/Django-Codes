from django.shortcuts import render,redirect
from .forms import CategoryForm
# Create your views here.
def AddCategory(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("AddCategory")
    else:
        form=CategoryForm()
    return render(request,"add_category.html",{'form':form})
