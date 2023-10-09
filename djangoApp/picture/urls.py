from django.urls import path
from .views import PictureCreateView,PictureListView,PictureDeleteView,PictureUpdateView


urlpatterns = [
    path('upload/', PictureCreateView.as_view(), name='picture_upload'),
    path('', PictureListView.as_view(), name='picture_list'),
     path('<int:pk>/delete/', PictureDeleteView.as_view(), name='picture_delete'),
     path('<int:pk>/edit/', PictureUpdateView.as_view(), name='picture_edit'),
]