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
        
    }

    return render(request, 'dashboard.html', context)

class CategoryList(ListView):
    model = Category
    context_object_name = " Categories"
    template_name = 'categories.html'
    
# class CreateCategory(Createview):
#     model = Category
#     fields = ['name']
#     success_url= '/staff/categories'
#     template_name = 'categories.html'

def viewStaff(request):
    context = {
        'staff': Staff.objects.all()
        
    }
    return render(request, 'staff.html', context)

def staffDetails(request, id):
    user= User.objects.get(pk = id)
    context = {
        'staff': Staff
        
    }
    return render(request, 'staff_details.html', context)

class staffDetails(DetailView):
    model= User
    template_name = 'staff_details.html'
    context_object_name = "staff"

class CreateStaff(CreateView):
    model = Staff
    fields = '__all__'
    success_url = '/staff/staff'
    template_name = 'staff_Details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Staff"
        return context

