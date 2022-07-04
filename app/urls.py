from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('register_user/',views.register_user,name='register_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('profile/',views.personal_profile,name='profile'),
    path('publish_order/',views.publish_order,name='publish_order'),
    path('buy_order', views.buy_order, name='buy_order'),
    path('orders_list/',views.orders_list,name='orders_list'),
    path('buyorders_list',views.buyorders_list,name='buyorders_list'),
    path('order/<int:pk>/',views.order_details,name='order_details'),
    path('buyorder/<int:pk>/',views.buyorder_details, name='buyorder_details'),
    path('order/<int:pk>/purchase/',views.purchase,name='purchase'),
    path('profile/analytics/', views.analytics, name='analytics'),
    path('order/<int:pk>/sale/',views.sale, name='sale'),
]