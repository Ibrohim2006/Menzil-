from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from yaml import serialize

from .models import Icon, Contact
from .serializers import IconSerializers, ContactSerializers


class ContactViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: ContactSerializers(many=True)},
        operation_description="Get all contact messages",
        tags=['Contact']
    )
    def ContactView(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializers(contacts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class IconViewSet(ViewSet):
    @swagger_auto_schema(
        response={200: IconSerializers(many=True)},
        operation_description="Get all icon",
        tags=['Icon']
    )
    def Icon_View(self, request):
        icon = Icon.objects.all()
        serializer = IconSerializers(icon, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
