from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


urlpatterns = [







    path('chrome/', views.chrome, name='chrome'),
   


    path('facebook/', views.FACEBOOK, name='facebook'),

    path('facebooksision/', views.FACEBOOKSISION, name='facebooksision'),





    path('', views.index_view, name='index_view'),




    path('commandes/', views.command, name='command'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('formation/', views.formation, name='formation'), 
    path('addproduct/', views.addaproduct, name='addproduct'),
    path('update_product/<int:my_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:my_id>/', views.delete_product, name="delete_product"),
    path('inscription/', views.inscription, name='inscription'),
    path('login/', views.tenant_login, name='tenant_login'),


    path('tenantsuperuser/', views.tenantsuperuser,name='tenantsuperuser'),
    path('createtenant/', views.createtenant,name='createtenant'),




    # رابط صفحة النجاح الخاصة بكل منتج
    path('success/<int:my_id>/', views.SUCCESS, name='success'),
   # path('success/', views.SUCCESS,name='success'),

    path('user/', views.user,name='user'),
    path('orders/', views.orders,name='orders'),
    path('update_orders/<int:my_id>/', views.update_orders, name="update_orders"),
    path('delete_orders/<int:my_id>/', views.delete_orders, name="delete_orders"),
    path('addorders/', views.addorders,name='addorders'),

    path('products/', views.products,name='products'),

    path('pixel/', views.pixel,name='pixel'),
    path('edit_pixel/<int:pixel_id>/', views.edit_pixel, name='edit_pixel'), 

    path('storecharging/', views.storecharging,name='storecharging'),


    path('plan/', views.plan,name='plan'),
    path('payment/', views.payment,name='payment'),
    path('subscriptions/', views.subscriptions,name='subscriptions'),
    
    path('design/', views.design,name='design'),
    path('storecharging/', views.storecharging,name='storecharging'),
    path('design/', views.design,name='design'),
    path('designstore/', views.designstore,name='designstore'),
    path('update_designstore/<int:my_id>/', views.update_designstore, name="update_designstore"),
    path('design/delete/<int:my_id>/',  views.delete_designstore, name='delete_designstore'),


    path('settings/', views.settings,name='settings'),
    path('domain/', views.domain,name='domain'),

    path('product/<int:my_id>/', views.PRODUCTURL,name='add_prodact'),

    path('addlivraison/', views.addlivraison,name='addlivraison'),
    path('livraison/', views.livraison,name='livraison'),
    path('update_livraison/<int:my_id>/', views.update_livraison, name="update_livraison"),
    path('delete_livraison/<int:my_id>/', views.delete_livraison, name="delete_livraison"),
  

    path('serial_sahlaboost/', views.serial_sahlaboost, name='serial_sahlaboost'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)