from django.db import models

# Create your models here.
class Product(models.Models):
    title = models.CharField(max_length=255) 
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Order(models.Models):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_CHOICES = [
        ('PAYMENT_PENDING', 'P'),
        ('PAYMENT_COMPLETE', 'C'),
        ('PAYMENT_FAILED', 'F')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField()


class Customer(models.Models):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        ('MEMBERSHIP_BRONZE', 'Bronze'),
        ('MEMBERSHIP_SILVER', 'Silver'),
        ('MEMBERSHIP_GOLD', 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # emailfield
    phone = models.CharField(max_length=255) 
    birth_date = models.DateField(null=True) # datefield
    
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES)



 