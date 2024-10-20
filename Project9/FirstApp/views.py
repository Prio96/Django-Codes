from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
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

def set_session(request):
    data={
        'name':'Karim',
        'age':15,
        'nationality':'Indian'
    }
    request.session.update(data)
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    return render(request,'set_session.html')

def get_session(request):
    if 'name' in request.session and 'age' in request.session and 'nationality' in request.session:
        name=request.session.get('name','Guest')
        age=request.session.get('age',"Age unknown")
        nationality=request.session.get('nationality')
        request.session.modified=True
        return render(request,'get_session.html',{'name':name,'age':age,'nationality':nationality})
    else:
        return HttpResponse("Your session has expired. Log In Again")

def del_session(request):
    # del request.session['name']
    # del request.session['age']
    request.session.flush()
    return render(request,'del_session.html')
    
    
