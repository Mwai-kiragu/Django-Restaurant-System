from django.db import models

# Create your models here.
class Staff(models.Model):
    number= models.IntergerField()
    gender= models.CharField(max_length=25)
    salary= models.IntergerField()
    address= models.CharField()
    department= models.TextField(blank=False, null=False)
    working_hours= models.IntergerField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Reservation(models.Model):
    table_number= models.IntergerField(blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time= models.DateTimeField(auto_now_add=True)
    number_of_people= models.IntergerField()
    RESERVATION_STATUSES=(
        ('expired', 'Expired')
        ('active', 'Active')
        ('complete', 'Complete')
    )
    status= models.CharField(max_length=100, choices=RESERVATION_STATUSES)

class Order(models.Model):
    ORDER_STATUSES(
        ('pending', 'Pending')
        ('completed', 'Completed')
    )
    status= models.CharField(max_length=100, choices=ORDER_STATUSES)
    order_number= models.IntergerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cost= models.IntegerField()
    is_delivery= models.BooleanField()
    staff_id= models.ForeignKey(Staff, on_delete=models.CASCADE)

class Menu(models.Model):
    MENU_ORDER(
        ('food', 'Food')
        ('drinks', 'Drinks')
    )

    food_type= models.CharField(max_length=100, choices=MENU_ORDER)
    category_id= models.ForeignKey(Category, on_delete=models.CASCADE)
    item= models.CharField(max_lenght=100)
    quantity= models.IntegerField(blank=False)

class OrderMenu(models.Model):
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity= models.IntegerField(blank=false)

class Payments(models.Model):
    PAYMENT_STATUSES(
        ('pending', 'Pending')
        ('completed', 'Completed')
    )
    status= models.CharField(max_length=100, choices=PAYMENT_STATUSES)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    
    PAYMENT_METHOD(
        ('mpesa', 'Mpesa')
        ('cash', 'Cash')
        ('credit card', 'Credit Card')
    )
    payment_mode= models.CharField(max_length=100, choices=PAYMENT_METHOD)

class Delivery(models.Model):
    AREA(
        ('cbd', 'CBD')
        ('within nairobi', 'Within Nairobi')
        ('outside nairobi', 'Outside Nairobi')
    )
    location_group= models.CharField(max_length=100, choices=AREA)
    delivery_fee= models.IntegerField(blank=False)

class OrderDelivery(models.Model):
    customer_id= models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    location= models.TextField()

    LOCATION_DELIVERY(
        ('pending', 'Pending')
        ('enroute', 'Enroute')
        ('completed', 'Completed')
    )

    status= models.CharField(max_length=100, choices=LOCATION_DELIVERY)
    delivery_id= models.ForeignKey(Delivery, on_delete=models.CASCADE)

class Review(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    message= models.TextField()
    stars= models.IntegerField(max_length=5)
