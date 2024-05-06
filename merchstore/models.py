from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        "ProductType", on_delete=models.SET_NULL, null=True, related_name="product_type"
    )
    owner = models.ForeignKey("user_management.Profile", on_delete=models.CASCADE, related_name="owner", null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    STOCK_CHOICES = {
        "Available" : "Available",
        "On Sale" : "On Sale",
        "Out of Stock" : "Out of Stock",
    }
    
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=12, choices=STOCK_CHOICES, default=STOCK_CHOICES["Available"])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore:product_detail", args=[str(self.pk)])

    class Meta:
        ordering = ["name"]


class Transaction(models.Model):
    buyer = models.ForeignKey("user_management.Profile", null=True, on_delete=models.SET_NULL, related_name="buyer")
    product = models.ForeignKey("Product", null=True, on_delete=models.SET_NULL, related_name="product")
    amount = models.IntegerField()
    
    STATUS_CHOICES = {
        "On Cart" : "On Cart",
        "To Pay" : "To Pay",
        "To Shop" : "To Shop",
        "To Receive" : "To Receive",
        "Delivered" : "Delivered",
    }

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} {self.product.name} bought by {self.buyer.display_name}'