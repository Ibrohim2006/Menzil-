from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet
from .models import AboutCompanyModel
from .serializers import AboutCompanySerializer
from rest_framework.response import Response
from rest_framework import status


class HomeViewSet(ViewSet):
    def about_company(self, request, *arg, **kwargs):
        header = AboutCompanyModel.objects.all().first()
        serializer = AboutCompanySerializer(header, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)