from rest_framework import serializers
from .models import Icon, Contact


class ContactSerializers(serializers):
    model = Contact
    field = ['id', 'name', 'email', 'message']


class IconSerializers(serializers):
    model = Icon
    field = ['id','image']

