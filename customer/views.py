from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import LoginForm, RegisterForm, RandomForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from .models import *
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.

def home(request):
    context={
        "register_form": RegisterForm(),
        "login_form" : LoginForm(),

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

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset_confirm.html", context={"password_reset_form":password_reset_form})


def password_reset_request(request):
    password_reset_form = PasswordResetForm(request.POST)
    if password_reset_form.is_valid():
        data = password_reset_form.cleaned_data['email']
        send_mail(
            'Ssup',
            'Reset Jamaa',
            'gg@gmail.com',
            [data],
            fail_silently=False,
        )
        return render(request=request, template_name="password/password_reset_confirm.html", context={})