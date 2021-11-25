from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from customer.models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def dashboard(request):
    
    context = {
        'users': User.objects.all()
    }

    return render(request, 'dashboard.html', context)

def viewStaff(request):
    context = {
        'staff': Staff_list.objects.all()
        
    }
    return render(request, 'staff.html', context)

def viewTable(request):
    context = {
        'table' : Table.objects.all()
    }
    
    return render(request, 'table.html', table)

def staffDetails(request, id):
    user= User.objects.get(pk = id)
    context = {
        'staff': Staff
        
    }
    return render(request, 'staff.html', context)


class StaffList(ListView):
    model= Staff
    template_name = 'staff.html'
    context_object_name = "staff_list"

class CreateStaff(CreateView):
    model = Staff
    fields = ['username','staff_number', 'gender', 'salary', 'address', 'department', 'working_hours', ]
    success_url = '/staff/staff'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Staff"
        return context
class CategoryList(ListView):
    model = Category
    context_object_name  ="categories"
    template_name = 'categories.html'

class CreateCategory(CreateView):
    model = Category
    fields = ['name']
    success_url = '/staff/categories'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Category"
        return context

# class CategoryUpdate(UpdateView):
#     model = Category
#     fields = ['name']
#     success_url = '/staff/categories'
#     template_name = 'board_form.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Update Category"
#         return context

class TableList(ListView):
    model = Table
    context_object_name = "tables"
    template_name = "tables.html"
    
class CreateTable(CreateView):
    model = Table
    fields = ['table_number', 'is_taken']
    success_url = '/staff/tables'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Table"
        return context
    
# class TableUpdate(UpdateView):
#     model = Table
#     fields = ['name']
#     success_url = '/staff/table'
#     template_name = 'board_form.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Update Table"
#         return context

class ReservationList(ListView):
    model = Reservation
    context_object_name = "reservations"
    template_name = "reservations.html"
    
class CreateReservation(CreateView):
    model = Reservation
    fields = ['table', 'user', 'people', 'status']
    template_name = "board_form.html"
    success_url = '/staff/reservations'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Reservation"
        return context
    
class OrderList(ListView):
    model = Order
    context_object_name = "orders"
    template_name = "orders.html"
    
class CreateOrder(CreateView):
    model = Order
    fields = ['order_number', 'status', 'user', 'cost', 'is_delivery', 'staff']
    template_name = "board_form.html"
    success_url = '/staff/orders'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Order"
        return context

class MenuList(ListView):
    model = Menu
    context_object_name = "menu_list"
    template_name = "menu.html"

class CreateMenu(CreateView):
    model =  Menu
    fields = ['food_type', 'category', 'item', 'quantity']
    template_name = "board_form.html"
    success_url = '/staff/menu'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Menu"
        return context
    
class PaymentList(ListView):
    model = Payments
    context_object_name = "payment"
    template_name = "payments.html"
    
class UpdatePayment(UpdateView):
    model = Payments
    fields = ['status', 'user', 'order', 'payment_mode']
    success_url = '/staff/payments'
    template_name = "board_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Payment" 
        return context
    
class DeliveryList(ListView):
    model = Delivery
    context_object_name = "deliveries"
    template_name = "deliveries.html"
    
class CreateDelivery(CreateView):
    model = Delivery
    fields = ['location_group', 'delivery_fee']
    success_url = '/staff/deliveries'
    template_name = "board_form.html"      
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Delivery"
        return context
    
class ReviewList(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "reviews.html"
    
class CreateReview(CreateView):
    model = Review
    fields = ['user', 'message', 'stars']
    success_url = '/staff/reviews'
    template_name = "board_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Review"
        return context
     