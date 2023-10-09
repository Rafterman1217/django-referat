
from django import forms
from content.forms import ContentForm
from .models import Picture


class PictureForm(ContentForm):
    class Meta:
        model = Picture
        fields = ['picture', 'show_since', 'show_until' ]    
        
    
class PictureEditForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['show_since', 'show_until']
        widgets = {
            'show_since': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'show_until': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
