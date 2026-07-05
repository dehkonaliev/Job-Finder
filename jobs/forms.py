# forms.py
from django import forms
from .models import Company, Job


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'desc', 'website']
        widgets = {'name': forms.TextInput(attrs={
                   'class': 'form-control',
                   'placeholder': 'Kompaniya nomi'
                                                }),
                   'desc': forms.Textarea(attrs={
                   'class': 'form-control',
                   'placeholder': 'Kompaniya haqida',
                   'rows': 4
                                                 }),
                   'website': forms.URLInput(attrs={
                   'class': 'form-control',
                   'placeholder': 'https://example.com'
                                                  }),
        }
        labels = {
            'name': 'Kompaniya nomi',
            'desc': 'Tavsif',
            'website': 'Vebsayt',
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'desc', 'category', 'location', 'salary_min', 'salary_max', 'job_type']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: Backend Developer'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Vakansiya haqida batafsil',
                'rows': 5
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: IT, Marketing'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: Toshkent'
            }),
            'salary_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minimal maosh'
            }),
            'salary_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maksimal maosh'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'title': 'Lavozim nomi',
            'desc': 'Tavsif',
            'category': 'Kategoriya',
            'location': 'Joylashuv',
            'salary_min': 'Minimal maosh',
            'salary_max': 'Maksimal maosh',
            'job_type': 'Ish turi',
        }

    def clean(self):
        cleaned_data = super().clean()
        salary_min = cleaned_data.get('salary_min')
        salary_max = cleaned_data.get('salary_max')

        if salary_min and salary_max:
            if salary_min > salary_max:
                raise forms.ValidationError(
                    'Minimal maosh maksimal maoshdan katta bo\'lishi mumkin emas!'
                )
        return cleaned_data