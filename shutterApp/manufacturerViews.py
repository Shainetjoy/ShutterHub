from django.shortcuts import render
from shutterApp.models import ManufacturersDtlClass

def displayProfile(request):
    u = request.user.id
    myProfile = ManufacturersDtlClass.objects.get( user_id = u)
    return render(request,'Manufacturer/myProfile.html',{"myProfile":myProfile})


def updateProfile(request,id):
    print(id,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    return render(request,'Manufacturer/updateProfile.html')






# def updateProduct(request, product_Id):
#     upProduct = ShutterDtls.objects.get(product_Id=product_Id)
#     ShutterAddForm = addShutter(instance=upProduct)
#     if request.method == 'POST':
#         ShutterAddForm = addShutter(request.POST, request.FILES, instance=upProduct)
#         if ShutterAddForm.is_valid():
#             ShutterAddForm.save()
#             return redirect('viewProduct')
#     return render(request, 'admin/UpdateProduct.html', {'ShutterAddForm': ShutterAddForm})
