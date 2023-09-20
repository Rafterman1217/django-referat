
from django import forms
from django.utils import timezone


class ContentForm(forms.ModelForm):
        
    def clean_dates(self):
        show_until = self.cleaned_data['show_until']
        now = timezone.now()
        show_since = self.cleaned_data['show_since']

        if show_until <= now:
            raise forms.ValidationError("Das Datum muss in der Zukunft liegen.")
        
        if show_since >=  self.cleaned_data['show_until']:
            raise forms.ValidationError("Das Datum muss nach dem Bis-Datum liegen.")
        
        return show_until, show_since
    

    
