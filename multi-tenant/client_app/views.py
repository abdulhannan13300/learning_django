from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Employee

def index(request):
    return HttpResponse(f'<h1> {request.tenant} index</h1>')
 
def create_employee(request, name):
    employee = Employee(name = name)
    employee.save()

    return HttpResponse(f'<h1> {request.tenant} employee create </h1>')