from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(attrs={
                'pattern': '[0-9]{10}',
                'title': '10-digit phone number'
            }),
        }