from django.urls import path
from . import views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('employee_register/',views.dealer_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('contact/', views.contact, name="contact"),
     path('product/',views.product, name='product'),
     path('profile/',views.profile, name='profile'),
     path('order/',views.order, name='order'),
     path('feedback/',views.feedback, name='feedback'),
     path('about/',views.about, name='about')
]