from django.views.generic import ListView
from text.models import Text

class TextListView(ListView):
    model = Text
    template_name = 'picture_list.html' 
    context_object_name = 'texts' 

    def get_queryset(self):
         return Text.objects.all()

