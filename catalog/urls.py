from django.urls import path
from .views import CategoryViewSet, ProductViewSet, MaterialViewSet

category_list = CategoryViewSet.as_view({'get': 'list'})
product_list = ProductViewSet.as_view({'get': 'list'})
product_detail = ProductViewSet.as_view({'get': 'retrieve'})
material_list = MaterialViewSet.as_view({'get': 'list'})
material_detail = MaterialViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('materials/', material_list, name='material-list'),
    path('materials/<int:pk>/', material_detail, name='material-detail'),
]
