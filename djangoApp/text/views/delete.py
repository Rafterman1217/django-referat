from django.urls import reverse_lazy
from django.views.generic import DeleteView
from text.models import Text

class TextDeleteView(DeleteView):
    model = Text
    template_name = 'text/text_confirm_delete.html'
    success_url = reverse_lazy('text_list')  
