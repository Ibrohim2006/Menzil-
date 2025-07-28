from modeltranslation.translator import TranslationOptions, translator
from .models import AboutCompanyModel, OurKeysModel


class AboutCompanyTranslationOptions(TranslationOptions):
    fields = ['title', 'description']

class OurKeysTranslationOptions(TranslationOptions):
    fields = ['title', 'name', 'description']

translator.register(AboutCompanyModel, AboutCompanyTranslationOptions)
translator.register(OurKeysModel, OurKeysTranslationOptions)
