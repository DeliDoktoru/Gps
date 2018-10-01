from django.core.validators import validate_email
from .models import Employee,Employer

def FormLogin(a):
    m=""
    if a.get("email") and  a.get("pass") :
        m+=checkEmptyData(a)
        m+=validateEmail(a.get("email"))
    else:
        return "Eksik Bilgi! "
    return m

def FormRegister(a):
    m=""
    if a.get("email") and a.get("name") and a.get("pass") and a.get("pass1"):
        m+=checkEmptyData(a)
        m+=validateEmail(a.get("email"))
        m+=checkUniqEmail(a.get("email"))
        m+=equalPassCheck(a.get("pass"),a.get("pass1"))
        m+checkUniqToken(a.get("token"))
    else:
        return "Eksik Bilgi! "
    return m    

def checkEmptyData(a):
    for val in list(a):
        if not val[1]:
            return "Alanların Doldurulması Gerekmektedir. "
    return ""

def validateEmail(a):  
    try:
        validate_email(a)
    except:
        return "Geçerli Mail Adresi Giriniz! "
    return ""
    
   
def equalPassCheck(a,b):    
    if a!=b:
        return "Şifreler Eşleşmiyor! "
    return ""    

def checkUniqEmail(a):
    if Employer.objects.filter(mail=a):
        return "Bu Mail Adresi Zaten Kullanılıyor! "
    return ""

def checkUniqToken(a):
    if Employer.objects.filter(token=a):
        return "Bu Token Adresi Zaten Kullanılıyor! "
    return ""
    