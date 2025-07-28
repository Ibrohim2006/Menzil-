from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updates_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Icon(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField('icon/', blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
