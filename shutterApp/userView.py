from django.shortcuts import render, redirect

from shutterApp.forms import Order
from shutterApp.models import ShutterDtls, OrderItems, Customer


def ProductCatalog(request):
    products = ShutterDtls.objects.all()
    return render(request, 'User/Product_Catalog.html', {'products': products})


# def BookProduct(request,product_Id ):
#     item = ShutterDtls.objects.get(product_Id=product_Id)
#     Product_Name = item.product_Name
#     product_Id = item.product_Id
#     description = item.description
#     Product_price = item.price
#     BookingItems.objects.create(product_Id = product_Id, Product_Name = Product_Name,Product_price = Product_price,description=description)
#
#     return render(request,'User/Booking.html',
#                   {"item":item})

def orderitems(request, product_Id):
    u = request.user.id
    customer = Customer.objects.filter(user__id= u).values()
    customer_name = customer[0]['Name']
    form = Order()
    if request.method == 'POST':
        item = ShutterDtls.objects.get(product_Id=product_Id)
        Product_Name = item.product_Name
        product_Id = item.product_Id
        Product_price = item.price
        form = Order(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = u
            data.Buyer_Name= customer_name
            data.Product_price = Product_price
            data.product_Id = product_Id
            data.Product_Name = Product_Name
            data.save()
            return redirect('viewOrders')
    return render(request,'User/orderitems.html', {'form': form})



def viewOrders(request):
    orderDtlz = OrderItems.objects.filter(user = request.user.id)

    return render(request,'User/viewOrder.html',{'orderDtlz':orderDtlz})