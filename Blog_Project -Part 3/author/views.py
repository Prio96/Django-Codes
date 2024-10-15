from typing import Any
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from new_post.models import NewPost
from django.urls import reverse_lazy
# Create your views here.
def Register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("HomePage")
    else:
        form=RegisterForm()
    return render(request,"register.html",{'form':form,'type':'Register'})

# def Log_in(request):
#     if request.method=='POST':
#         form=AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             user_name=form.cleaned_data['username']
#             user_pass=form.cleaned_data['password']
#             user=authenticate(username=user_name,password=user_pass)
#             if user is not None:
#                 messages.success(request,'Logged in successfully')
#                 login(request,user)
#                 return redirect("Profile")
#         else:
#             messages.warning(request,"Login credentials don't match")
#             return redirect("Login")
#     else:
#         form=AuthenticationForm()
#     return render(request,"register.html",{'form':form,'type':'Login'})

@login_required
def Profile(request):
    data=NewPost.objects.filter(author=request.user)
    return render(request,"profile.html",{'posts':data,'type':'Profile'})

@login_required
def Edit_Profile(request):
    if request.method=='POST':
        form=ChangeUserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully")
            print(form.cleaned_data)
    else:
        form=ChangeUserForm(instance=request.user)
    return render(request,"update_profile.html",{'form':form,'type':'Update Profile'})

@login_required
def Pass_Change(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            messages.success(request,"Password Changed Successfully")
            form.save()
            update_session_auth_hash(request,request.user)
            print(form.cleaned_data)
            return redirect("Profile")
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,"pass_change.html",{'form':form,'type':'Change Your Password'})

# @login_required
# def Logout(request):
#     logout(request)
#     return redirect("Login")

class AuthorLoginView(LoginView):
    template_name='register.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']="Login"
        return context
    def get_success_url(self):
        return reverse_lazy('Profile')
    def form_invalid(self, form):
        messages.warning(self.request,"Login Credentials don't match")
        return super().form_invalid(form)
    def form_valid(self, form):
        messages.success(self.request,"Logged In Successfully")
        return super().form_valid(form)
    
# class AuthorLogoutView(LogoutView):
#     template_name='register.html'
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['type']="Logout"
#         return context
#     def get_success_url(self):
#         return reverse_lazy('Login')
        
       
    
    
