
from content.forms import ContentForm
from .models import Text
from django import forms

class TextForm(ContentForm):
    class Meta:
        model = Text
        fields = ['text', 'show_since', 'show_until' ]    
        



class TextEditForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['show_since', 'show_until']
        widgets = {
            'show_since': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'show_until': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
