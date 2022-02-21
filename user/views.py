from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection
# Create your views here.
def home(request):
    status = False
    if request.method == 'POST':
        Trip=request.POST.get("trip","")
        Tour=request.POST.get("tour","")
        Name = request.POST.get("name", "")
        DOB = request.POST.get("dob", "")
        Contact = request.POST.get("contact", "")
        Email = request.POST.get("email", "")
        Vechile = request.POST.get("vechile", "")
        Pas = request.POST.get("pas", "")
        Message = request.POST.get("message", "")
        res = booking(tour=Tour,trip=Trip,name=Name, contact=Contact,dob=DOB, email=Email,vechile=Vechile,pas=Pas, message=Message)
        res.save()
        status = True
        return HttpResponse("<script>alert('Thanks,WE CALL YOU SOON FOR MORE DETAIL`S...');window.location.href='/user/'</script>")
    return render(request, 'user/index.html', {'S': status})

def aboutus(request):
    return render(request,'user/aboutus.html')

def mybooking(request):
    return render(request,'user/mybooking.html')

def myprofile(request):
    user=request.session.get('userid')
    pdata=profile.objects.filter(email=user)
    return render(request, 'user/myprofile.html',{"profile":pdata})

def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Mobile=request.POST.get("mobile","")
        Email=request.POST.get("email","")
        Message=request.POST.get("msg","")
        res=contact(name=Name,contact=Mobile,email=Email,message=Message)
        res.save()
        status=True
        #return HttpResponse("<script>alert('Thanks For Enquiry..');window.location.href='/user/contactus/'</script>")
    return render(request,'user/contactus.html',{'S':status})

def signup(request):
    status=False
    if request.method=='POST':
        name=request.POST.get("name","")
        DOB=request.POST.get("dob","")
        Mobile=request.POST.get("mobile","")
        Email=request.POST.get("email","")
        Password=request.POST.get("passwd","")
        ProfilePhoto=request.FILES['myfile']
        Address=request.POST.get("address","")
        d=profile.objects.filter(email=Email)

        if d.count()>0:
            return HttpResponse("<script>alert('You are already registered..');window.location.href='/user/signup/'</script>")
        else:
            res=profile(name=name,dob=DOB,mobile=Mobile,email=Email,passwd=Password,myfile=ProfilePhoto,address=Address)
            res.save()
            return HttpResponse("<script>alert('You are registered successfully..');window.location.href='/user/signup/'</script>")

        #return HttpResponse("<script>alert('Thanks For SignUp..');window.location.href='/user/signup/';</script>")
    return render(request,'user/signup.html')

def signin(request):
    if request.method=='POST':

        uname=request.POST.get("uname")
        passwd=request.POST.get("passwd")
        checkuser=profile.objects.filter(email=uname,passwd=passwd)
        if(checkuser):
            request.session['userid']=uname
            return HttpResponse("<script>alert('Logged In Successfully');window.location.href='/user/';</script>")

        else:
            return HttpResponse("<script>alert('UserID or Password is Incorrect');window.location.href='/user/signin';</script>")
    return render(request,'user/signin.html')

def process(request):
    userid = request.session.get('userid')
    if userid is not None:
                return render(request,'user/process.html', {"alreadylogin": True})
    else:
        return HttpResponse("<script>window.location.href='/user/signin/'</script>")


def logout(request):
    del request.session['userid']
    return HttpResponse("<script>window.location.href='/user/home/'</script>")