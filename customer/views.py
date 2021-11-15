from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import LoginForm, RegisterForm, RandomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

def home(request):
    context={
        "register_form": RegisterForm(),
        "login_form" : LoginForm()
    }
    return render(request, 'home.html', context)

    return HttpResponse("This is my page")

def loginUser(request):
    
    if request.method =='GET':
        return HttpResponseRedirect('/')
    
    else:
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user= authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                context = {}
                
                return HttpResponseRedirect('staff/profile')
            
            else:
                messages.error(request, 'Login not Successful')
                return HttpResponseRedirect(request.Meta.get('HTTP_REFERER'))
            
        else:
            returnHttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
def registerUser(request):
    if request.method == "GET":
    
        data = {
            'success': False,
            'message': "Should be a post request"
        }
        
        return JsonResponse(data)
    
    else:
        
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            name= form.cleaned_data['name']
            age= form.cleaned_data['age']
            password= form.cleaned_data['password']
            email= form.cleaned_data['email']
            
            user = User()
            user.username = name
            user.age = age
            user.email = email
            user.set_password(password)
            user.save()
            
            login(request, user)
            # mail_message = "Hello, "+name+" .Welcome to my Restaurant where you settle with your favorite dish."
            # send_mail(
            #     'Welcome to my Restaurant',
            #     mail_message,
            #     "admin@gmail.com",
            #     [email],
            #     fail_silently= False    
            # )
            
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        data = {'success': True, 'message':"Register Successful, Redirecting..."}
        return JsonResponse(data)

