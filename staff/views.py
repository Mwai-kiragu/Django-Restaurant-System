from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from customer.models import *

# Create your views here.
def dashboard(request):
    
    context = {
        
    }

    return render(request, 'dashboard.html', context)

def sidebar(request):
    context={
        
    }
    return render(request, 'sidebar.html', context)