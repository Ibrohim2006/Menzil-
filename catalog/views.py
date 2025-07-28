from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Material
from .serializers import CategorySerializer, ProductSerializer, MaterialSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CategoryViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all categories",
        responses={200: CategorySerializer(many=True)}
    )
    def list(self, request):
        categories = CategorySerializer(Category.objects.all(), many=True)
        return Response(categories.data, status=status.HTTP_200_OK)


class ProductViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all products",
        responses={200: ProductSerializer(many=True)}
    )
    def list(self, request):
        products = ProductSerializer(Product.objects.all(), many=True)
        return Response(products.data, status=status.HTTP_200_OK)


class MaterialViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all materials",
        responses={200: MaterialSerializer(many=True)}
    )
    def list(self, request):
        materials = MaterialSerializer(Material.objects.all(), many=True)
        return Response(materials.data, status=status.HTTP_200_OK)
