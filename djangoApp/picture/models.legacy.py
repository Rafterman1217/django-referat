from django.db import models

# Create your models here.
class Picture(models.Model):

    picture = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    show_until = models.DateTimeField()
    show_since = models.DateTimeField()
    

class Text(models.Model):

    text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    show_until = models.DateTimeField()
    show_since = models.DateTimeField()
    