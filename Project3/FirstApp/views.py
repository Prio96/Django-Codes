from django.shortcuts import render
from datetime import *
# Create your views here.
def home(request):
    d={'Name':'Rahim','Age':15,'Lst':["I","love","Python"],'Date':datetime.now(),'Courses':[
        {
            'id':0,
            'name':'Python',
            'fee':5000,
            'description':"a course about Python"
        },
        {
            'id':1,
            'name':'Django',
            'fee':6000,
            'description':"a course about the framework of Python, Django"
        },
        {
            'id':2,
            'name':'Javascript',
            'fee':3000,
            'description':""
        }
    ]}
    return render(request,"FirstApp/home.html",d)
