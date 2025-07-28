from django.db import models


class AboutCompanyModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='about_company/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class OurKeysModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='our_keys/', blank=True, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"