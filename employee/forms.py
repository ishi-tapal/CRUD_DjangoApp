from django import forms
from .models import Employee

class Employeeform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'emp_id' : 'Employee_ID',
            'emp_name' : 'Name',
            'emp_contact' : 'Contact',
            'emp_email' : 'Email id',
            'emp_desg': 'Designation '
        }

    
    def __init__(self,*args,**kwargs):
        super(Employeeform,self).__init__(*args,**kwargs)
        self.fields['emp_desg'].empty_label = "Select"
        self.fields['emp_email'].required = False