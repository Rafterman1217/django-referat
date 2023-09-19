
from django import forms
from .models import Picture
from django.utils import timezone


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture', 'show_until']    
        
        
    def clean_show_until(self):
        show_until = self.cleaned_data['show_until']
        now = timezone.now()

        if show_until <= now:
            raise forms.ValidationError("Das Datum muss in der Zukunft liegen.")

        return show_until