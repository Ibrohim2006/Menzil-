from django.urls import path
from .views import ContactViewSet, IconViewSet

urlpatterns = [
    path('contact/', ContactViewSet.as_view({'post': 'create'}), name='contact'),
    path('icon/', IconViewSet.as_view({'get': 'list'}), name='icon'),
]