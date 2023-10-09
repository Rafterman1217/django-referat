from django.urls import reverse_lazy
from django.views.generic import UpdateView
from picture.forms import PictureEditForm
from picture.models import Picture

class PictureUpdateView(UpdateView):
    model = Picture
    template_name = 'picture/picture_update_form.html'
    form_class = PictureEditForm
    success_url = reverse_lazy('picture_list')

