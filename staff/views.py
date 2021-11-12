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