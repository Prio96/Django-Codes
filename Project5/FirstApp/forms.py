from django import forms
from django.core import validators
#widgets=field to html input
class contactForm(forms.Form):
    name=forms.CharField(label="Username",required=False,disabled=False,help_text="Name can not exceed more than 70 characters",widget=forms.Textarea(attrs={'id':'user_name','class':'class1','placeholder':'Type your name...'}))
    file=forms.FileField(required=False)
    email=forms.EmailField()
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()#DecimalField is used for more precise values like 12.00
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()#FloatField does not give precise values like 12.00000000008
    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.CharField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    SIZE=[('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=SIZE,widget=forms.RadioSelect)
    ING=[('P','Pepperoni'),('S','Sausage'),('M','Mushroom')]
    ingredients=forms.MultipleChoiceField(choices=ING,widget=forms.CheckboxSelectMultiple)
    # Date input must be given in MM/DD/YYYY format

class StudentForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(5,message="Your name must have at least 5 characters"),validators.MaxLengthValidator(60,message="Your name can not exceed 60 characters")])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Your Email is invalid")])
    age=forms.IntegerField(validators=[validators.MinValueValidator(10,message="You must be at least 10 years old"),validators.MaxValueValidator(40,message="Your age can not exceed 40")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=".pdf",message="File must be a .pdf file")])
    # def clean(self):
    #     cleaned_data=super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Your name must have at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must have .com in it")

class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data=super().clean()
        valpass1=self.cleaned_data['password']
        valpass2=self.cleaned_data['confirm_password']
        if valpass1!=valpass2:
            raise forms.ValidationError("Passwords don't match")