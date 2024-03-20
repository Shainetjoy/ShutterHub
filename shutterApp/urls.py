from django.urls import path
from shutterApp import views,adminViews




urlpatterns = [
    path('',views.shutterIndex,name= "shutterIndex"),
    path('shutterSignin',views.shutterSignin,name= "shutterSignin"),
    path('shutterSignUp',views.shutterSignUp,name= "shutterSignUp"),
    path('shutterAdminIndex',views.shutterAdminIndex,name= "shutterAdminIndex"),
    path('shutterUserIndex',views.shutterUserIndex,name= "shutterUserIndex"),
    path('ManufacturersIndex',views.ManufacturersIndex,name= "ManufacturersIndex"),
    path('SalesIndex',views.SalesIndex,name= "SalesIndex"),
    path('addShutter',adminViews.Shutter_Add,name ="addShutter"),



]