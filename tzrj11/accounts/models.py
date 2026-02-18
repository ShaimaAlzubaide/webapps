from django.db import models
STORE_CHOICES = [
    ('Shein', 'Shein'),
    ('Amazon', 'Amazon'),
    ('Noon', 'Noon'),
    ('AliExpress','AliExpress'),
    ('book time', 'book time')
    
]

class Store(models.Model):
    name = models.CharField(max_length=100, choices=STORE_CHOICES, unique=True)

    def __str__(self):
        return self.name

#العميل
class Customer(models.Model):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    location = models.URLField() 
    
    
    def __str__(self):
        return self.name

# accounts/models.py

#المن\وب
class Agent(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='agent_images/')
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    location = models.URLField()
    description = models.TextField()
    password = models.CharField(max_length=100)
    stores = models.ManyToManyField('Store', related_name='agents')

    def __str__(self):
        return self.name



class Order(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='order_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    required_number = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    
    
    def __str__(self):
        return self.service_name
# 4. السلات
class ShoppingCart(models.Model):
    store_name = models.CharField(max_length=100, choices=STORE_CHOICES)
    payment_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    customers = models.ManyToManyField(Customer, related_name='shopping_carts')

    def __str__(self):
        return f"Cart for {self.store_name}"

# 5. التخفيضات
class Offer(models.Model):
    image = models.ImageField(upload_to='offer_images/')
    offer_type = models.CharField(max_length=100)
    stores = models.ManyToManyField(Store, related_name='offers')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.offer_type
