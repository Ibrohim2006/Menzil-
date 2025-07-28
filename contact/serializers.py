from rest_framework import serializers
from config import settings
from .models import Icon, Contact


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message']


class IconSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()

    class Meta:
        model = Icon
        fields = ['id', 'name', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data
