from django.shortcuts import render,HttpResponse
from general import *
from general.models import ContactModel,LoginModel

from django.core.mail import send_mail
from django.conf import  settings


# Create your views here.
import random
def index(request):
    return render(request, "index.html")
def pre(request):
    return render(request, "home.html")
def aboutus(request):
    return render(request, "aboutUs.html")
def logIn(request):
    return render(request, "logIn.html")
def visa(request):
    return render(request, "visa.html")
def contacts(request):
    return render(request,"contacts.html")
def services(request):
    return render(request,"services.html")

def bus(request):
    return render(request,"bus.html")
def train(request):
    return render(request,"train.html")
def flight(request):
    return render(request,"flight.html")
def feedback(request):
    return render(request,"feedback.html")
def booking(request):
    return render(request,"booking.html")
def SaveData(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        mob=request.POST['mob']
        query=request.POST['query']
        data=ContactModel(name=name,email=email,mobile=mob,queue=query)
        data.save()
        return HttpResponse("<script>alert('Thanks Data Saved Successfully');window.location.href='/contacts'</script>")
    else:
        return HttpResponse("<script>alert('OHH Something Went Wrong');window.location.href='/contacts'</script>")



def loginData(request):
 try:
    if request.method == 'POST':
        aid=request.POST['aid']
        passwd=request.POST['passwd']
        lg=LoginModel.objects.get(aid=aid)
        if lg.aid==aid and lg.passwd==passwd:
            request.session['aid']=aid
            return HttpResponse("<script>alert('Logged In');window.location.href='/dashboard/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid UserId or Password');window.location.href='/logIn/'</script>")
 except LoginModel.DoesNotExist:
     return HttpResponse("<script>alert('Invalid UserId or Password');window.location.href='/logIn/'</script>")


def forget(request):
    return render(request,'forget.html')
def otp(request):
    return render(request,'otp.html')
def newpass(request):
    return render(request,'newpass.html')
def forgetData(request):
 try:
    if request.method == "POST":
        adminid=request.POST['adminid']
        data=LoginModel.objects.get(aid=adminid)
        if data.aid==adminid:
            x1 = int(random.random()*12)
            x2 = int(random.random() * 14)
            x3 = int(random.random() * 16)
            x4 = int(random.random() * 12)
            code=str(x1) + str(x2) + str(x3) + str(x4)
            send_mail(subject="otp Verification from EVO-TOUR",message="ur otp is this"+code+"regards EVO TOUR portal",from_email=settings.EMAIL_HOST_USER,recipient_list=[adminid],fail_silently=False)
            request.session['code']=code
            return HttpResponse("<script>alert('UR otp is sent on "+adminid+"email address. Check It');window.location.href='/otp/'</script>")

        else:
            return HttpResponse("<script>alert('Not Reg Mail');window.location.href='/forget/'</script>")

 except LoginModel.DoesNotExist:
     return HttpResponse("<script>alert('Not Reg Mail');window.location.href='/forget/'</script>")
def otpData(request):
    if request.method == "POST":
        otp=request.POST['otp']
        code=request.session['code']
        if otp==code:
            request.session['adminid']=request.session['adminid']
            return HttpResponse("<script>alert('Invalid otp');window.location.href=/newpass/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid otp');window.location.href='/forget/'</script>")

