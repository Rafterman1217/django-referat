from django.urls import path
from .views import TextCreateView,TextListView,TextUpdateView,TextDeleteView

urlpatterns = [
    path('upload/', TextCreateView.as_view(), name='text_upload'),
    path('',TextListView.as_view(),name='text_list'),
    path('<int:pk>/edit/', TextUpdateView.as_view(), name='text_edit'),    
    path('<int:pk>/delete/', TextDeleteView.as_view(), name='text_delete'),    
]