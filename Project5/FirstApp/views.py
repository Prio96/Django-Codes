from django.shortcuts import render

from .forms import contactForm,StudentForm


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    if request.method=='POST':
        print(request.POST)
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'about.html',{'name':name,'email':email,'select':select})
    else:
        return render(request,'about.html')
def form(request):
    return render(request,'form.html')

def django_form(request):
    if request.method=='POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file=form.cleaned_data['file']
            # with open('./FirstApp/upload/'+ file.name,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form=contactForm()
    return render(request,'django_form.html',{'form':form})

def studentform(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            # file=form.cleaned_data['file']
            # with open('./FirstApp/upload/'+ file.name,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form=StudentForm()
    return render(request,'django_form.html',{'form':form})