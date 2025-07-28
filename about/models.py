from django.db import models


class AboutCompanyModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.Textfield()
    image = models.ImageField(upload_to='about_company/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
