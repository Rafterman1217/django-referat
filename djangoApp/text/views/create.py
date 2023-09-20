from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from text.forms import TextForm

from text.models import Text

class TextCreateView(CreateView):
    model = Text
    form_class = TextForm  
    template_name = 'text/text_form.html'
    success_url = reverse_lazy('text_list')
