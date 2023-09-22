from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return f"products/{self.id}"
    
    def __str__(self):
        return str(self.title)