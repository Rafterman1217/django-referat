from django.urls import reverse_lazy
from django.views.generic import DeleteView
from picture.models import Picture

class PictureDeleteView(DeleteView):
    model = Picture
    template_name = 'picture/picture_confirm_delete.html'
    success_url = reverse_lazy('picture_list')  
