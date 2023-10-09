from django.urls import reverse_lazy
from django.views.generic import UpdateView
from text.forms import TextEditForm
from text.models import Text

class TextUpdateView(UpdateView):
    model = Text
    template_name = 'text/text_update_form.html'
    form_class = TextEditForm
    success_url = reverse_lazy('text_list')

