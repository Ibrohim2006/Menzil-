from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
    

class Partners(models.Model):
    title = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.title

