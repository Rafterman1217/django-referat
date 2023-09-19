from django.shortcuts import render
from django.views import View
from picture.models import Picture
from django.utils import timezone

class HomeView(View):
    template_name = 'home/index.html' 
    def get(self,request):
    
        return render(request,self.template_name)



class TaskView(View):
    template_name = 'tasks.html' 
    def get(self,request):
    
        return render(request,self.template_name)




