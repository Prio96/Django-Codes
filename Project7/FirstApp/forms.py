from django import forms
from FirstApp.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'#fields=['fieldname','fieldname','fieldname']
        #exclude=['fieldname']
        labels={
            'name':'StudentName',
            'roll':'StudentRoll'
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter your name...'})
        }
        help_texts={
            'name':"Write your full name"
        }
        error_messages={
            'name':{'required': "Your name is required"}
        }
    
        