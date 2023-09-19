from django.urls import path
from .views import PictureCreateView,PictureListView,PictureListValidView

urlpatterns = [
    path('upload/', PictureCreateView.as_view(), name='picture_upload'),
    path('pictures/', PictureListView.as_view(), name='picture_list'),
    path('pictures/valid/', PictureListValidView.as_view(), name='picture_list_valid'),
]