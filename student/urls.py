from django.urls import path
from .views import index,contact_us,register


urlpatterns = [

    path('',index,name='home'),
    path('contact-us/',contact_us,name='contact-us'),
    path('register/',register,name='register'),
]