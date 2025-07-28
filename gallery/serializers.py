from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Gallery, Partners
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = 'title', 'image'

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = 'title', 'image'

