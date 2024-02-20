from django.db import models

class Customer(models.Model):
    product_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name