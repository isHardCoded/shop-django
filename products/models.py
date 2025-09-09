from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def get_image(self):
        return self.image.url

    def __str__(self):
        return self.name
