from django.conf import settings
from rest_framework import serializers
from .models import AboutCompanyModel, OurKeysModel


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanyModel
        fields = ['id', 'title', 'description', 'image']


class NestedKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurKeysModel
        fields = ['id', 'name', 'description', 'image']


class OurKeysSerializer(serializers.ModelSerializer):
    keys = serializers.SerializerMethodField()

    class Meta:
        model = OurKeysModel
        fields = ['id', 'title', 'keys']

    def get_keys(self, obj):
        request = self.context.get('request')
        keys = OurKeysModel.objects.all()
        return NestedKeysSerializer(keys, many=True, context={'request': request}).data
