from django.shortcuts import render, redirect
# from django.http import redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import Booking
from CameraApp.models import Patient
from BookingApp.models import Doctor, Payment
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe


# Create your views here.
###############################################################################################
################################     CREATING A BOOKING             ###########################
###############################################################################################
@csrf_exempt    
def BookingView(request, pk):
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(400 *100)
    description = '#incubating Inventions'

    if request.method == 'POST':        
        # print(request.POST)

        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingCity = request.POST['stripeBillingAddressCity']
            billingPostcode = request.POST['stripeBillingAddressZip']
            billingCountry =request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingCity = request.POST['stripeShippingAddressCity']
            shippingPostcode = request.POST['stripeShippingAddressZip']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            customer = stripe.Customer.create(
                        email= email,
                        source = token
                )
            charge = stripe.Charge.create(
                        amount = stripe_total,
                        currency = 'inr',
                        description = description,
                        customer = customer.id,
                )
            print('charge values', charge)
            try:
                person = Patient.objects.get(patient_id = pk)
                p = Payment.objects.create(payment_id = token, user = person.username, amount = stripe_total, paid = True)
                p.save()
            except Exception:
                print('error occured while saving payment data')

        except Exception:
            print('no payment')





        form = BookingForm(request.POST)       

        if form.is_valid():
            person = Patient.objects.get(patient_id = pk)
            p_name = person.username    
            p_id = person.patient_id     
            d = request.POST['doctor']
            doctor = Doctor.objects.get(id = d)            
            
            book = Booking.objects.create(patient= p_name,                                        
                                          doctor = doctor,
                                          description = request.POST['description'],
                                          Booking_time = request.POST['Booking_time'],
                                        #   amount = 400
                                            )
            print('booking created')
            book.save()


            ################     STRIPE CODE     ##############



            # return HttpResponse('booking data added to db')
            return render(request, 'BookingApp/payment.html', {'book':book})

        else:
            b = Booking.objects.all().latest('pk')
            b.payment_status = True
            b.save()

            return redirect('BookingApp:payment_sucess')
    
    else:
        form = BookingForm()
    return render(request, 'BookingApp/booking.html', {'form':form, 'data_key':data_key, 'stripe_total':stripe_total, 'description':description })

###############################################################################################
################################       SHOW A BOOKING             #############################
###############################################################################################

def ShowBookingView(request, pk):
    a = Booking.objects.get(id = pk)
    print(a)
    return render(request, 'BookingApp/show_booking.html',{'a':a}) 

###############################################################################################
################################       PAYMENT SUCCESS            #############################
###############################################################################################

def PaymentSuccess(request):
    return render(request,  'BookingApp/payment_done.html')

 
 
###############################################################################################
############################           EXTRAS          ########################################
###############################################################################################
'''
def ExtrasView(request):
    a = Booking.objects.filter(patient__username__icontain = name2) 
    b = Booking.objects.filter(patient__username__contain = name2) 
    c = Booking.objects.filter(doctor__username__exact = name2)  
    d = Booking.objects.filter(doctor__username__iexact = name2) 
    print(a) 
'''     