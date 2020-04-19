from django.conf.urls import url
from . import views
from django.urls import path 

urlpatterns = [
    path('', views.home, name="home" ),
    path('product/', views.products_url, name='product' ) ,
    path('customer/<str:obj_id>/', views.customer_url,name="customer" ) , # here obj_id is number of the pertucal object for a url
    path('create_order/',views.createorder,name='create_order' ),
    path('create_customer/' ,views.createcustomer,name='create_customer'),
    path('update_order/<str:obj_id>',views.updateorder ,name='update_order'),
    path('delete_order/<str:obj_id>',views.deleteorder ,name='delete_order'), #name is for dymanic url routing.
    path('login/',views.loginpage ,name='login'),
    path('register/',views.register ,name='register'),
    path('logout/',views.logoutUser ,name='logout'),
    path('userpage/',views.userPage ,name='userpage'),
]


