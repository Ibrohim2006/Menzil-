from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet
from .models import AboutCompanyModel, OurKeysModel
from .serializers import AboutCompanySerializer, OurKeysSerializer
from rest_framework.response import Response
from rest_framework import status



class HomeViewSet(ViewSet):
    def about_company(self, request, *arg, **kwargs):
        about_company = AboutCompanyModel.objects.all().first()
        serializer = AboutCompanySerializer(about_company, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def our_keys(self, request, *arg, **kwargs):
        our_keys = OurKeysModel.objects.all().first()
        serializer = OurKeysSerializer(our_keys, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

