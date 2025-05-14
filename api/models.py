from django.db import models

# Create your models here.
class Merchandise(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/merchandise/', null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    merchandise = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    phone_number = models.CharField(max_length=8)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.merchandise.name}(s) with phone number {self.phone_number} created at {self.created_at}"