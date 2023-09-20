from django.db import models

# Create your models here.
class Content(models.Model):
    
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    show_until = models.DateTimeField()
    show_since = models.DateTimeField()
    
    class Meta:
        abstract = True
        ordering = ['-created_at']

