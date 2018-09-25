from django.shortcuts import render
from django.http import HttpResponse
from .serializers import EmployeeSerilazer,EmployerSerilazer
from .models import Employee,Employer
from rest_framework import viewsets

# Create your views here.
def home(request):
    return render(request, 'Pages/home.html')
def login(request):  
    if request.method == 'POST':
        if request.POST.get('type')=='k':

            return HttpResponse('Kayıt Oluşturuldu!')                  
    elif request.method == 'GET':    
        return render(request, 'Pages/login.html')
 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilazer

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerilazer