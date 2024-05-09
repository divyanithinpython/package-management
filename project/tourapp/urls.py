from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from.import views as v

urlpatterns = [
    path('',v.Index,name="Index"),
    path('search/',v.search_packages,name="search_packages"),
    path('addpackage/',v.add_package,name="add_package"),
    path('register/',v.useregister,name="register"),
    path('login/',v.user_login,name="login"),
    path('vendor_register/',v.vendorregister,name="vendorregister"),
    path('vendor_login/',v.vendorlogin,name="vendorlogin"),
    path('home/',v.home,name="home"),
    path('book/<int:package_id>/',v.book,name="book"),
    
    path('payment/',v.payment,name="payment"),
    path('main',v.main,name="main"),
    
    
    path('package/<int:pk>/package_details/',v.packgedetail,name="packgedetail"),

    path('tourpackage/',v.tour,name="tour"),
    
    path('aboutus/',v.about,name="about"),
    path('packages/',v.packagelist,name="packagelist"),
    path('userlogout/',v.uslogout,name="uslogout"),
    path('vendorlogout/',v.vendor_logout,name="vendor_logout"),
    path('package/<int:pk>/edit/',v.editt,name='editt'),
    path('package/<int:pk>/delete/',v.delte,name='delte'),
    path('payment/success/',v.payment_success_callback,name="payment_success_callback"),
    path('confirmation/',v.booking_confirmation,name="booking_confirmation"),
    path('booklist/',v.bookinglist,name="bookinglist"),
    
    
    
    
    
    
    
    
    
    
]