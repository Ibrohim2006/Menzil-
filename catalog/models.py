from django.db import models
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=255)
    )

    def __str__(self):
        return self.name

class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=255),
        description = models.TextField()
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
class Material(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=255),
        description = models.TextField()
    )
    category = models.ForeignKey(Category, related_name='materials', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='materials/')

    def __str__(self):
        return self.name