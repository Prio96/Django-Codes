from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course(request):
    return HttpResponse("This is courses page.")
def about(request):
    return HttpResponse("This is about page of FirstApp")
def home(request):
    return HttpResponse("This is FirstApp Home Page")
