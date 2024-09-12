from django.shortcuts import render,redirect
from .forms import SignupForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.
def home(request):
    return render(request,"home.html")

def make_acc(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignupForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account created successfully')
                # messages.warning()
                # messages.info()
                # messages.danger()
                form.save()
                print(form.cleaned_data)
        else:
            form=SignupForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect("profile")

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name,password=userpass)
                if user is not None:
                    login(request,user)
                    return redirect("profile")
        else:
            form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect("profile")

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=ChangeUserData(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Account updated successfully')
                # messages.warning()
                # messages.info()
                # messages.danger()
                form.save()
                print(form.cleaned_data)
        else:
            form=ChangeUserData(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else:
        return redirect("login")
    
def user_logout(request):
    logout(request)
    return redirect("login")

def pass_change1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user)
                print(form.cleaned_data)
                return redirect("profile")
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect("login")
    
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user)
                print(form.cleaned_data)
                return redirect("profile")
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect("login")
    