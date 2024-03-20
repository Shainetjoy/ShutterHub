from django.shortcuts import render,redirect
from . forms import addShutter
def Shutter_Add(request):
    ShutterAddForm = addShutter()
    if request.method == 'POST':
        ShutterAddForm = addShutter(request.POST,request.FILES)
        if ShutterAddForm.is_valid():
            ShutterAddForm.save()
            return redirect('shutterAdminIndex.html')
    return render(request,'admin/addShutter.html',{'ShutterAddForm':ShutterAddForm})