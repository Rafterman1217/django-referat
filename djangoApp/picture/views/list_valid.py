from django.shortcuts import render
from django.views import View
from picture.models import Picture
from django.utils import timezone

class PictureListValidView(View):


    template_name = 'picture/picture_list_valid.html' 



    def get(self,request):
        
        
        pictures=Picture.objects.filter(show_since__lte=timezone.now()) 
        pictures= pictures.filter(show_until__gte=timezone.now()) 
        
        return render(request,self.template_name,context={"pictures":pictures})