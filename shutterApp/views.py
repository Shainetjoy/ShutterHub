from django.contrib import auth,messages
from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import UserRgistration,CustomerREgistration

# Create your views here.
def shutterIndex(request):
    return render(request,'shutterIndex.html')



def shutterSignin(request):
    if request.method == 'POST':
        username = request.POST.get('Uname')
        password = request.POST.get('pword')
        user = auth.authenticate(username = username,password=password)
        if user is not None and  user.is_staff:
            login(request,user)
            return redirect('shutterAdminIndex')
        elif user is not None and user.is_Manufacturers:
            login(request, user)
            return redirect('ManufacturersIndex')

        elif user is not None and user.is_user:
            login(request,user)
            return redirect('shutterUserIndex')


        elif user is not None and user.is_Sales:
            login(request,user)
            return redirect('SalesIndex')

        else:
            messages.info(request,"Invalid credentials ")


    return render(request,'shutterSignin.html')


def shutterSignUp(request):
    UserRegistration = UserRgistration()
    CustomerRegister = CustomerREgistration() 
    return render(request,'shutterSignUp.html',{'UserRegistration':UserRegistration,'CustomerRegister':CustomerRegister })


def shutterAdminIndex(request):
    return render(request,'shutterAdminIndex.html')


def shutterUserIndex(request):
    return render(request,'shutterUserIndex.html')


def ManufacturersIndex(request):
    return render(request,'ManufacturersIndex.html')




def SalesIndex(request):
    return render(request,'SalesIndex.html')