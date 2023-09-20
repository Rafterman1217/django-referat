from django.urls import path
from .views import TextCreateView,TextListView

urlpatterns = [
    path('upload/', TextCreateView.as_view(), name='text_upload'),
    path('',TextListView.as_view(),name='text_list')

]