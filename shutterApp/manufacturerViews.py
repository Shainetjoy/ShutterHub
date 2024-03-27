from django.shortcuts import render, redirect

from shutterApp.forms import ManufacturersDtlForms
from shutterApp.models import ManufacturersDtlClass

def displayProfile(request):
    u = request.user.id
    myProfile = ManufacturersDtlClass.objects.get( user_id = u)
    return render(request,'Manufacturer/myProfile.html',{"myProfile":myProfile})


def updateProfile(request,id):
    Muser = ManufacturersDtlClass.objects.get(user_id = id)
    Muserform = ManufacturersDtlForms(instance = Muser )
    if request.method == 'POST':
        Muserform = ManufacturersDtlForms(request.POST,instance = Muser)
        if Muserform.is_valid():
            Muserform.save()
            return redirect('displayProfile')
    return render(request,'Manufacturer/updateProfile.html',{"Muserform":Muserform})


def viewProducts