from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    path('dashboard', dashboard, name='dashboard'),
    path('categories', CategoryList.as_view(), name="categories"),
    path('category/create', CreateCategory.as_view(), name="create.category"),
    # path('category/update/<pk>', CategoryUpdate.as_view(), name="category.update"),
    path('staff', StaffList.as_view(), name='staff'),
    path('staff/create', CreateStaff.as_view(), name="create.staff"),
    path('staff/<id>', staffDetails, name="staff.details"),
    path('table/create', CreateTable.as_view(), name = 'create.table'),
    path('tables', TableList.as_view(), name="tables"),
    # path('category/update/<pk>', TableUpdate.as_view(), name="table.update"),
    path('reservations', ReservationList.as_view(), name="reservations"),
    path('reservation/create', CreateReservation.as_view(), name= 'create.reservation'),
    path('orders', OrderList.as_view(), name="orders"),
    path('order/create', CreateOrder.as_view(), name= 'create.order'),
    path('menu', MenuList.as_view(), name = "menu"),
    path('menu/create', CreateMenu.as_view(), name = 'create.menu'),
    path('payments', PaymentList.as_view(), name="payments"),
    path('payment/create', CreatePayment.as_view(), name='create.payment'),
    path('deliveries', DeliveryList.as_view(), name="deliveries"),
    path('delivery/create', CreateDelivery.as_view(), name= 'create.delivery'),
    path('reviews', ReviewList.as_view(), name="reviews"),
    path('review/create', CreateReview.as_view(), name= 'create.review'),
]