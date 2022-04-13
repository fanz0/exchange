from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('register_user/',views.register_user,name='register_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('profile/',views.personal_profile,name='profile'),
    path('publish_order/',views.publish_order,name='publish_order'),
    path('orders_list/',views.orders_list,name='orders_list'),
    path('order/<int:pk>/',views.order_details,name='order_details'),
    path('order/<int:pk>/purchase/',views.purchase,name='purchase'),
    path('profile/analytics/',views.analytics,name='analytics'),
]