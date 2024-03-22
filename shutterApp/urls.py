from django.urls import path
from shutterApp import views, adminViews,userView,manufacturerViews

urlpatterns = [
    path('', views.shutterIndex, name="shutterIndex"),
    path('shutterSignin', views.shutterSignin, name="shutterSignin"),
    path('CustomerRegistrationFun', views.CustomerRegistrationFun, name="CustomerRegistrationFun"),
    path('ManufacturersDtlFun', views.ManufacturersDtlFun, name="ManufacturersDtlFun"),
    path('Sales_TeamModelClass', views.Sales_TeamModelClass, name="Sales_TeamModelClass"),
    path('shutterAdminIndex', views.shutterAdminIndex, name="shutterAdminIndex"),
    path('shutterUserIndex',views.shutterUserIndex, name="shutterUserIndex"),
    path('ManufacturersIndex', views.ManufacturersIndex, name="ManufacturersIndex"),
    path('SalesIndex', views.SalesIndex, name="SalesIndex"),
    path('addShutter', adminViews.Shutter_Add, name="addShutter"),
    path('viewProduct', adminViews.viewProduct, name="viewProduct"),
    path('updateProduct/<int:product_Id>', adminViews.updateProduct, name="updateProduct"),
    path('deleteProduct/<int:product_Id>', adminViews.remove, name="deleteProduct"),
    path('deleteProduct/<int:product_Id>', adminViews.remove, name="deleteProduct"),
    path('ProductCatalog', userView.ProductCatalog, name="ProductCatalog"),
    path('orderitems/<int:product_Id>/', userView.orderitems, name="orderitems"),
    path('view_order', adminViews.view_order, name="view_order"),
    path('viewOrders', userView.viewOrders, name="viewOrders"),
    path('updateStatus/<int:product_Id>', adminViews.updateStatus, name="updateStatus"),



    path('displayProfile', manufacturerViews.displayProfile, name="displayProfile"),
    path('updateProfile/<int:id>/', manufacturerViews.updateProfile, name="updateProfile"),










]
