from django.urls import path
from django.contrib import admin
from . views import index, create_employee

urlpatterns = [
    path('', index ,name='client_index'),
    path('admin/',admin.site.urls),
    path('createemp/<name>', create_employee, name = "create_employee")
]