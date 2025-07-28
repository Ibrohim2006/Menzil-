from django.urls import path
from .views import ContactViewSet, IconViewSet

urlpatterns = [
    path('contact/', ContactViewSet.as_view({'get': 'ContactView'}, name='contact')),
    path('icon/', IconViewSet.as_view({'get': 'IconView'}, name='icon')),
]
