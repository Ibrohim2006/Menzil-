from django.urls import path
from .views import CategoryViewSet, ProductViewSet, MaterialViewSet

category_list = CategoryViewSet.as_view({'get': 'list'})
product_list = ProductViewSet.as_view({'get': 'list'})
material_list = MaterialViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('products/', product_list, name='product-list'),
    path('materials/', material_list, name='material-list'),
]
