from django import forms
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
    name=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data['name']
        valemail=self.cleaned_data['email']
        if len(valname)<10:
            raise forms.ValidationError("Your name must have at least 10 characters")
        if '.com' not in valemail:
            raise forms.ValidationError("Your email must have .com in it")