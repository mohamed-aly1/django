
from django.urls import path, include
from . import views 

urlpatterns = [
    
    path("home0/", views.home1 , name="home1"),
    path("home/", views.home , name="home"),
    path("menu/", views.menu , name="menu"),
    path("profile/",views.profile, name="profile"),
    path('cart/', views.add_to_cart, name='add_to_cart'),
    path("signup/" ,views.register , name="signup"),
    path("login/",views.login, name="login"), # type: ignore
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail')
    ]
    
