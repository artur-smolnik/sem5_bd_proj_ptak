from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('client/', views.client),
    path('workerlogin/',views.workerlogin),
    path('workerpage/',views.workerpage,),
    path('client/allstuff/',views.show_allstuff),
    path('client/clientstuff/',views.client_clientstuff),
    path('client/clientstuff/dupa/',views.post_client),
    path('workerlogin/verify/',views.workerlogin_verify),
    path('workerpage/addstuff/',views.workerpage_addstuff),
    path('workerpage/deletestuff/',views.workerpage_deletestuff),
    path('workerpage/allstuff/',views.show_allstuff),
    path('workerpage/returnstuff/verify/',views.workerpage_returnstuff_verify),
    path('workerpage/returnstuff/',views.workerpage_returnstuff),
    path('workerpage/clientstuff/',views.workerpage_clientstuff),

]   
