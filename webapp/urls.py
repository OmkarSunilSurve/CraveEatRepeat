from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orderplaced/',views.orderplaced),
    path('restaurant/',views.restuarent,name='restuarant'),
    path('register/user/',views.customerRegister,name='register'),
    path('login/user/',views.customerLogin,name='login'),
    path('login/restaurant/',views.restLogin,name='rlogin'),
    path('register/restaurant/',views.restRegister,name='rregister'),
    path('profile/restaurant/',views.restaurantProfile,name='rprofile'),
    path('profile/user/',views.customerProfile,name='profile'),
    path('user/create/',views.createCustomer,name='ccreate'),
    path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    path('restaurant/create/',views.createRestaurant,name='rcreate'),
    path('restaurant/update/<int:id>/',views.updateRestaurant,name='rupdate'),
    path('restaurant/orderlist/',views.orderlist,name='orderlist'),
    path('restaurant/menu/',views.menuManipulation,name='mmenu'),
    path('logout/',views.Logout,name='logout'),
    path('restaurant/<int:pk>/',views.restuarantMenu,name='menu'),
    path('checkout/',views.checkout,name='checkout'),
    path('restaurant/customerorder/',views.customerorder,name='customerorder'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="webapp/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="webapp/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/ ',
         auth_views.PasswordResetConfirmView.as_view(template_name="webapp/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="webapp/password_reset_done.html"),
         name="password_reset_complete"),
     path("handlerequest/", views.handlerequest, name="HandleRequest"),
     


]