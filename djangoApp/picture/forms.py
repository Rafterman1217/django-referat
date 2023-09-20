
from content.forms import ContentForm
from .models import Picture


class PictureForm(ContentForm):
    class Meta:
        model = Picture
        fields = ['picture', 'show_since', 'show_until' ]    
        
    
