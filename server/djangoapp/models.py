from django.db import models
from django.contrib.auth.models import User


class CarMake(models.Model):
    """Model representing a car manufacturer"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class CarModel(models.Model):
    """Model representing a specific car model"""
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    TRUCK = 'Truck'
    
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (TRUCK, 'Truck'),
    ]
    
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
    
    class Meta:
        ordering = ['make__name', 'name', 'year']
        unique_together = ['make', 'name', 'year']


class Dealer(models.Model):
    """Model representing a car dealer"""
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    short_desc = models.TextField(blank=True)
    full_desc = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"
    
    class Meta:
        ordering = ['state', 'city', 'name']


class Review(models.Model):
    """Model representing a customer review for a dealer"""
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    car_year = models.IntegerField(null=True, blank=True)
    review_text = models.TextField()
    sentiment = models.CharField(max_length=20, default='neutral')  # positive, negative, neutral
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Review by {self.customer.username} for {self.dealer.name}"
    
    class Meta:
        ordering = ['-created_at']
