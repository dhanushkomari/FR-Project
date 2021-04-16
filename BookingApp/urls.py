from django.urls import path
from . import views

app_name = "BookingApp"

urlpatterns = [
    # path('', views.BookingView, name = 'booking'),
    # path('', views.test, name = 'test'), 
    path('create/<str:pk>', views.BookingView, name = 'create-booking'),
    path('all/<str:pk>', views.ShowBookingView, name = 'single-booking'),
    path('payment-sucess', views.PaymentSuccess, name = 'payment_sucess'),
    path('phonepe', views.phonepeView, name = 'phonepe')
]
