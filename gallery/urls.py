from django.urls import path
from .views import GalleryViewSet, PartnersViewSet  

gallery_list = GalleryViewSet.as_view({'get': 'list'})
partners_list = PartnersViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('gallery/', gallery_list, name='gallery-list'),
    path('partners/', partners_list, name='partners-list'),
]