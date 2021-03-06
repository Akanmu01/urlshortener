from django.db import models

# Create your models here.
class Link(models.Model):
    original_url = models.URLField(help_text= "Add the original URL that you want to shorten.")
    key = models.CharField(max_length=20, unique= True, help_text= "Add any random characters of your choice to shorten it.")

    def __str__(self):
        return f"{self.key}"
        