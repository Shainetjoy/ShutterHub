from django.shortcuts import render
from .forms import UserRgistration,CustomerREgistration

# Create your views here.
def shutterIndex(request):
    return render(request,'shutterIndex.html')



def shutterSignin(request):
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