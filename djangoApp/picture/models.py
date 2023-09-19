from django.db import models

# Create your models here.
class Picture(models.Model):
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    picture = models.ImageField()
    show_until = models.DateTimeField()
    