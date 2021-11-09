from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Staff)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(OrderMenu)
admin.site.register(Payments)
admin.site.register(Delivery)
admin.site.register(OrderDelivery)
admin.site.register(Review)