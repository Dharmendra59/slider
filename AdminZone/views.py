from django.http import HttpResponse
from django.shortcuts import render
from general.models import ContactModel,LoginModel
from django.core.mail import  send_mail
from django.conf import settings
# Create your views here.
def dashboard(request):
    if request.session.has_key("aid"):
        return render(request,"AdminZone/dashboard.html")
    else:
        return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def contactmgmt(request):
    if request.session.has_key("aid"):
        data=ContactModel.objects.all()
        return render(request,"AdminZone/contactmgmt.html",{"data":data})
    return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def changepass(request):

        return render(request,"AdminZone/changepass.html")
def logout(request):
    del request.session["aid"]
    return HttpResponse("<script>window.location.href='/logIn/'</script>")

def feedbackmgmt(request):
    if request.session.has_key("aid"):
        return render(request,"AdminZone/feedbackmgmt.html")
    return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def bookingmgmt(request):
    if request.session.has_key("aid"):
        return render(request,"AdminZone/bookingmgmt.html")
    return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def delData(request,id):
    data=ContactModel.objects.get(id=id)
    data.delete()
    return HttpResponse("<script>alert('Record Deleted');window.location.href='/contactmgmt/'</script>")

def changeData(request):
    if request.session.has_key("aid"):
        if request.method=="POST":
            npass=request.POST["npass"]
            cpass = request.POST["cpass"]
            if npass==cpass:
                email=request.session["aid"]
                data=LoginModel.objects.get(aid=email)
                data.passwd=npass
                data.save()
                send_mail(subject="Change Password Updation",message="thanks pss is change"+npass+"and email address="+email+"",from_email=settings.EMAIL_HOST_USER,recipient_list=[email],fail_silently=False)
                return HttpResponse("<script>alert('PassChange');window.location.href='/logIn/'</script>")
            else:
                return HttpResponse("<script>alert(' Pls Confirm Pass');window.location.href='/changepass/'</script>")

    else:
        return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")