from django.shortcuts import render,redirect
from .forms import ProfileForm
# Create your views here.
def AddProfile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("AddProfile")
    else:
        form=ProfileForm()
    return render(request,'add_profile.html',{'form':form})
    