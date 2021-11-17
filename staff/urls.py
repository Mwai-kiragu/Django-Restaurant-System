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
    path('table/create', CreateCategory.as_view(), name = 'create.table'),
    path('table', TableList.as_view(), name="table"),
    path('category/update/<pk>', TableUpdate.as_view(), name="table.update"),
    
    
]