from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, ListView
from .models import TransactionModel,DEPOSIT,WITHDRAWAL,LOAN,LOAN_PAID
from .forms import DepositForm,WithdrawForm,LoanRequestForm
from django.http import HttpResponse
from datetime import *
#Ei view ke inherit kore deposit, withdraw, loan request er kaaj
class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name=''
    model=TransactionModel
    title=''
    success_url=''
    
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account, #goes to  __init__ of TransactionForm
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })
        
class DepositMoneyView(TransactionCreateMixin):
    form_class=DepositForm
    title='Deposit'
    
    def get_initial(self):
        initial={'transaction_type' : DEPOSIT}
        return initial

    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance+=amount
        
        account.save(
            update_fields=['balance']
        )
        
        messages.success(self.request, f"{amount}$ was deposited to your account successfully")
        return super().form_valid(form)
    
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class=WithdrawForm
    title='Withdraw'
    def get_initial(self):
        initial={'transaction_type' : WITHDRAWAL}
        return initial
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance-=amount
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request, f"{amount}$ was withdrawn from your account successfully")
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_Class=LoanRequestForm
    title='Request For Loan'
    
    def get_initial(self):
        initial={'transaction_type': LOAN}
        return initial
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        current_loan_count=TransactionModel.objects.filter(account=self.request.user.account,transaction_type=LOAN, loan_approval=True).count()#Number of loans of user approved by bank
        if current_loan_count>=3:
            return HttpResponse("You have crossed limit")
        messages.success(self.request,f"Loan request for amount {amount}$ has been made to admin")
        return super().form_valid(form)
    
class TransactionReportView(LoginRequiredMixin,ListView):
    template_name=""
    model=TransactionModel
    balance=0
    
    def get_queryset(self):
        queryset=super().get_queryset().filter(
            account=self.request.user.account
        )
        
        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date=datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date=datetime.strptime(end_date_str,"%Y-%m-%d").date()
            
            self.balance=TransactionModel.objects.filter(timestamp_date_gte=start_date, timestamp_data_lte=end_date)
        
        
        