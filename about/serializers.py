from django.conf import settings
from rest_framework import serializers
from .models import AboutCompanyModel, OurKeysModel


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanyModel
        fields = ['id', 'title', 'description', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data


class NestedKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurKeysModel
        fields = ['id', 'name', 'description', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data


class OurKeysSerializer(serializers.ModelSerializer):
    keys = serializers.SerializerMethodField()

    class Meta:
        model = OurKeysModel
        fields = ['id', 'title', 'keys']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
            data['name'] = getattr(instance, f'name_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data

    def get_keys(self, obj):
        request = self.context.get('request')
        keys = OurKeysModel.objects.all()
        return NestedKeysSerializer(keys, many=True, context={'request': request}).data
