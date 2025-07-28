from django.conf import settings
from rest_framework import serializers
from .models import AboutCompanyModel


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanyModel
        fields = ['id', 'title', 'description', 'image']