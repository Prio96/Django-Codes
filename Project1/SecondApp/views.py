from django.shortcuts import render
from django.http import HttpResponse

def course(request):
    return HttpResponse("This is second app courses page")

def about(request):
    return HttpResponse("This is second app about page")

def home(request):
    return HttpResponse("This is second app home page")
# Create your views here.
