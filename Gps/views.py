from django.shortcuts import render
from django.http import HttpResponse
from .serializers import EmployeeSerilazer,EmployerSerilazer
from .models import Employee,Employer
from rest_framework import viewsets
from django.core.validators import validate_email

# Create your views here.
def home(request):
    return render(request, 'Pages/home.html')
def login(request):  
    if request.method == 'POST':
        message="Kayıt Oluşturuldu!"
        if request.POST.get('type')=='k':
            try:
                validate_email( request.POST.get('email') )
            except:
                message="Geçerli Mail Adresi Giriniz!"
            try:
                if(request.POST.get('pass')!=request.POST.get('pass1')):
                    raise
            except:
                message="Şifreler Eşleşmiyor!"                   
            e=Employer(name=request.POST.get('name'),mail=request.POST.get('email'),password=request.POST.get('pass'),token=request.POST.get('csrfmiddlewaretoken'))
            e.save()
            return HttpResponse(message)                  
    elif request.method == 'GET':    
        return render(request, 'Pages/login.html')
 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilazer

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerilazer