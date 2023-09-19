from django.views.generic import ListView
from picture.models import Picture
from django.utils import timezone

class PictureListView(ListView):
    model = Picture
    template_name = 'picture_list.html' 
    context_object_name = 'pictures' 

    def get_queryset(self):
         return Picture.objects.all()

