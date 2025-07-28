from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Icon, Contact
from .serializers import ContactSerializer, IconSerializer


class ContactViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: ContactSerializer(many=True)},
        operation_description="Get all contact messages",
        tags=['Contact']
    )
    def list(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ContactSerializer,
        response={201: ContactSerializer},
        operation_description="Create new contact message",
        tags=['Contact']
    )
    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IconViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: IconSerializer(many=True)},
        operation_description="Get all icons",
        tags=['Icon']
    )
    def list(self, request):
        icons = Icon.objects.all()
        serializer = IconSerializer(icons, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
