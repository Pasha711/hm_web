# places/forms.py

from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        # session_key будемо заповнювати автоматично
        exclude = ['session_key']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад, "Найкраща кава у місті"'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'place_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кафе, Парк, Музей...'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адреса або район'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
