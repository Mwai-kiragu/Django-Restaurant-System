from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staff(User):
    staff_number= models.IntegerField(null=True, blank=True)
    GENDER_OPTIONS=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    # is_staff = models.BooleanField(default=True)   
    gender= models.CharField(max_length=25, choices=GENDER_OPTIONS)
    salary= models.IntegerField(null=True, blank=True)
    address= models.CharField(max_length=100)
    DEPARTMENT_OPTIONS=(
        ('waiter', 'Waiter'),
        ('chef', 'Chef'),
        ('admin', 'Admin')
    )
    department= models.CharField(max_length=50, choices=DEPARTMENT_OPTIONS)
    working_hours= models.IntegerField(default=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Table(models.Model):
    table_number= models.IntegerField(blank=False)
    is_taken= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reservation(models.Model):
    table= models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    people = models.IntegerField(default=2)
    RESERVATION_STATUSES=(
        ('expired', 'Expired'),
        ('active', 'Active'),
        ('complete', 'Complete')
    )
    status= models.CharField(default="active", max_length=100, choices=RESERVATION_STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    MAKE_ORDER=(
        ('pending', 'Pending'),
        ('completed', 'Completed')
    )
    status= models.CharField(default="pending", max_length=100, choices=MAKE_ORDER)
    order_number= models.IntegerField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    cost= models.IntegerField()
    is_delivery= models.BooleanField(default=False)
    staff= models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True, related_name="staff")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    MENU_ORDER=(
        ('food', 'Food'),
        ('drinks', 'Drinks')
    )

    food_type= models.CharField(max_length=100, choices=MENU_ORDER)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    item= models.CharField(max_length=100)
    quantity= models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderMenu(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity= models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payments(models.Model):
    PAYMENT_STATUSES=(
        ('pending', 'Pending'),
        ('completed', 'Completed')
    )
    status= models.CharField(default="pending", max_length=100, choices=PAYMENT_STATUSES)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    
    PAYMENT_METHOD=(
        ('mpesa', 'Mpesa'),
        ('cash', 'Cash'),
        ('credit card', 'Credit Card')
    )
    payment_mode= models.CharField(default="cash", max_length=100, choices=PAYMENT_METHOD)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Delivery(models.Model):
    AREA=(
        ('cbd', 'CBD'),
        ('within nairobi', 'Within Nairobi'),
        ('outside nairobi', 'Outside Nairobi')
    )
    location_group= models.CharField(max_length=100, choices=AREA)
    delivery_fee= models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderDelivery(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    location= models.TextField()

    LOCATION_DELIVERY=(
        ('pending', 'Pending'),
        ('enroute', 'Enroute'),
        ('completed', 'Completed')
    )

    status= models.CharField(default="pending", max_length=100, choices=LOCATION_DELIVERY)
    delivery_id= models.ForeignKey(Delivery, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    message= models.TextField(null=True,blank=True)
    stars= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
