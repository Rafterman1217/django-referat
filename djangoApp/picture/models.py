from django.db import models

from content.models import Content

# Create your models here.
class Picture(Content):

    picture = models.ImageField(upload_to='images/')

    