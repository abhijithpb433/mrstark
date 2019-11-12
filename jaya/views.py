from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.models import auth
from django.contrib import messages



# Create your views here.
def jayasurya(request):
    return render(request, "jithu.html", )


def abhijith(request):
    A = Product.objects.all()
    return render(request, 'haha.html', {'ob': A})


def jithu(request):
    return render(request, "index1.html")


def ajin(request):
    if request.method == 'POST':
        a=request.POST['username']
        b=request.POST['password']
        user=auth.authenticate(username=a,password=b)
        if user is not None:
            auth.login(request,user)
            return redirect("jaya:hhh")
        else:
            messages.error(request,'invaild data')

    return render(request, "login.html")


def deva(request):
    return render(request, "sign in.html")


def ajil(request):
    return render(request, "logged.html")
def vipin(request):

    auth.logout(request)
    return redirect('jaya:hhh')

def reg(request):
    return render(request,'register.html')
    # if request.method == 'POST':
       # a = request.POST['username']
        #b = request.POST['password']
        #c = request.POST['firstname']
        #d = request.POST['lastname']
        #e = request.POST['gmail']
        #user = auth.authenticate(username=a, password=b,firstname=c,lastname=d,gmail=e)