from django.db import models

# Create your models here.
class Merchandise(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/merchandise/', null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name