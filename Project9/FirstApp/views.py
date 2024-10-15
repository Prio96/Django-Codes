from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def home(request):
    response=render(request,"home.html")
    # response.set_cookie('name','Prio',max_age=60*3) The cookie will stay for 60*3 seconds or 180 seconds
    response.set_cookie('name','Prio',expires=datetime.now()+timedelta(days=7))
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,"get_cookie.html",{'name':name})

def del_cookie(request):
    response=render(request,"del_cookie.html")
    response.delete_cookie('name')
    return response
    
