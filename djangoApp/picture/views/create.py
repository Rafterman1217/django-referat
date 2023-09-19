from django.views.generic.edit import CreateView
from picture.forms import PictureForm
from picture.models import Picture
from django.urls import reverse_lazy

class PictureCreateView(CreateView):
    model = Picture
    form_class = PictureForm  
    template_name = 'picture/picture_form.html'
    success_url = reverse_lazy('picture_list')
