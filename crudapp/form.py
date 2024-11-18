from django.forms import forms,TextInput,EmailInput,NumberInput
from django import forms
from .models import Employee
class empform(forms.ModelForm):
    class Meta:
        model=Employee
        exclude=['upadated_at','Created_at']

        labels={'empname':'Employee Name','empemail':'Employee Email','empcontact':'Employee Contact','empcity':'Employee City','empsal':'Employee Salary'}

        widgets={
            'empname':TextInput(attrs={'class':'form-control'}),
            'empemail':EmailInput(attrs={'class':'form-control'}),
            'empcontact':NumberInput(attrs={'class':'form-control'}),
            'empcity':TextInput(attrs={'class':'form-control'}),
            'empsal':NumberInput(attrs={'class':'form-control'})
        }