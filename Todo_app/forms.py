from django import forms
from . models import todo

class todo_form(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['event','date']
        widgets = {
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control','placeholder':'mm/dd/yyyy'}),
        }