from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.views.generic import ListView
from .models import Content
from picture.models import Picture
from text.models import Text


class CombinedContentView(ListView):
    model = Content
    template_name = 'combined_content.html'
    context_object_name = 'combined_content_list'

    def get_queryset(self):

        pictures = Picture.objects.all()
        texts = Text.objects.all()

        pictures = pictures.filter(show_since__lte=timezone.now())
        pictures = pictures.filter(show_until__gte=timezone.now())

        texts = texts.filter(show_since__lte=timezone.now())
        texts = texts.filter(show_until__gte=timezone.now())

        for pic in pictures:
            pic.content_type = 'picture'
        for txt in texts:
            txt.content_type = 'text'

        combined_content = list(pictures) + list(texts)

        combined_content.sort(key=lambda x: x.created_at, reverse=True)
        return combined_content
