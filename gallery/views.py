from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Gallery, Partners
from .serializers import GallerySerializer, PartnersSerializer

class GalleryViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all gallery items",
        responses={200: openapi.Response(
            description="List of gallery items",
            examples={
                "application/json": {
                    "gallery": [
                        {"id": 1, "title": "Sample Gallery", "image": "/media/gallery/sample.jpg"}
                    ]
                }
            }
        )}
    )
    def list(self, request):
        gallery = GallerySerializer(Gallery.objects.all(), many=True).data
        return Response({'gallery': gallery}, status=status.HTTP_200_OK)

class PartnersViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all partner items",
        responses={200: openapi.Response(
            description="List of partners",
            examples={
                "application/json": {
                    "partners": [
                        {"id": 1, "title": "Sample Partner", "image": "/media/partners/sample.jpg"}
                    ]
                }
            }
        )}
    )
    def list(self, request):
        partners = PartnersSerializer(Partners.objects.all(), many=True).data
        return Response({'partners': partners}, status=status.HTTP_200_OK)   
