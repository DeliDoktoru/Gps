from django.shortcuts import render
from django.http import HttpResponse
from .serializers import EmployeeSerilazer,EmployerSerilazer
from .models import Employee,Employer
from rest_framework import viewsets
from .validator import FormRegister,FormLogin
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'Pages/home.html',{'a':request.session['mail']})
def login(request):  
    if request.method == 'POST':
        
        if request.POST.get('type')=='kayıt':
            message=FormRegister(request.POST)
            if message=="":
                e=Employer(name=request.POST.get('name'),mail=request.POST.get('email'),password=request.POST.get('pass'),token=request.POST.get('csrfmiddlewaretoken'))
                e.save()
                message="Kayıt Oluşturuldu! "  
            return HttpResponse(message)     
        elif request.POST.get('type')=='giris':
            message=FormLogin(request.POST)
            if message=="":
                tmp=Employer.objects.filter(mail=request.POST.get("email"),password=request.POST.get("pass") )
                if not tmp:
                    return HttpResponse("Email Yada Şifre Yanlış! ")            
                else:
                    request.session['id'] = tmp[0].id
                    request.session['mail'] = tmp[0].mail
                    request.session['token'] = tmp[0].token
                    request.session['name'] = tmp[0].name
                    return HttpResponse("Giriş Yapılıyor! ") 
    elif request.method == 'GET':    
        return render(request, 'Pages/login.html')
 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilazer

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerilazer