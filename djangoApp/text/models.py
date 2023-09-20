from django.db import models

from content.models import Content

# Create your models here.
class Text(Content):

    text = models.TextField(max_length=2000)

    