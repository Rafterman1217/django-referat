from django.urls import path
from .views import PictureCreateView,PictureListView

urlpatterns = [
    path('upload/', PictureCreateView.as_view(), name='picture_upload'),
    path('', PictureListView.as_view(), name='picture_list'),

]