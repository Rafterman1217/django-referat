
from content.forms import ContentForm
from .models import Text


class TextForm(ContentForm):
    class Meta:
        model = Text
        fields = ['text', 'show_since', 'show_until' ]    
        
    
