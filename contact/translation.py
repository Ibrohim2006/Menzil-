from modeltranslation.translator import translator, TranslationOptions
from .models import Icon



class IconTranslationOptions(TranslationOptions):
    fields = ['name',]


translator.register(Icon, IconTranslationOptions)
