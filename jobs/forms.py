# forms.py
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'desc', 'category', 'location', 'salary_min', 'salary_max', 'job_type']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Backend Developer'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Detailed job description',
                'rows': 5
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. IT, Marketing'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Tashkent'
            }),
            'salary_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minimum salary'
            }),
            'salary_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maximum salary'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'title': 'Job Title',
            'desc': 'Description',
            'category': 'Category',
            'location': 'Location',
            'salary_min': 'Minimum Salary',
            'salary_max': 'Maximum Salary',
            'job_type': 'Job Type',
        }

    def clean(self):
        cleaned_data = super().clean()
        salary_min = cleaned_data.get('salary_min')
        salary_max = cleaned_data.get('salary_max')

        if salary_min and salary_max:
            if salary_min > salary_max:
                raise forms.ValidationError(
                    'Minimum salary cannot be greater than maximum salary!'
                )
        return cleaned_data