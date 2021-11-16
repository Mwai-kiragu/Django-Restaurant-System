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

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    success_url = '/staff/categories'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Category"
        return context

class TableList(ListView):
    model = Table
    context_object_name = "table"
    template_name = "table.html"
    
class CreateTable(CreateView):
    model = Table
    fields = '__all__'
    success_url = '/staff/table'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Table"
        return context
    
class TableUpdate(UpdateView):
    model = Table
    fields = ['name']
    success_url = '/staff/table'
    template_name = 'board_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Table"
        return context