from django.urls import path
from .views import HomeViewSet

urlpatterns = [
    path('get_about_company/', HomeViewSet.as_view({'get': 'about_company'}), name= 'get_about_company'),
]