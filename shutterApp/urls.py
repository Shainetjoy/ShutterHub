from django.urls import path
from shutterApp import views




urlpatterns = [
    path('',views.shutterIndex,name= "shutterIndex"),
    path('shutterSignin',views.shutterSignin,name= "shutterSignin"),
    path('shutterSignUp',views.shutterSignUp,name= "shutterSignUp"),
    path('shutterAdminIndex',views.shutterAdminIndex,name= "shutterAdminIndex"),



]