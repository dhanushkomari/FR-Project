from django.shortcuts import render, redirect
# from django.http import redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import Booking
from CameraApp.models import Patient
from BookingApp.models import Doctor


# Create your views here.
###############################################################################################
################################     CREATING A BOOKING             ###########################
###############################################################################################
def BookingView(request, pk):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            person = Patient.objects.get(patient_id = pk)
            p_name = person.username            
            d = request.POST['doctor']
            doctor = Doctor.objects.get(id = d)            
            
            book = Booking.objects.create(patient= p_name,                                        
                                          doctor = doctor,
                                          description = request.POST['description'],
                                          Booking_time = request.POST['Booking_time']
                                            )
            book.save()
            return redirect('CameraApp:index')
        else:
            return HttpResponse('New data added')
    else:
        form = BookingForm()
    return render(request, 'BookingApp/booking.html', {'form':form})

###############################################################################################
################################       SHOW A BOOKING             #############################
###############################################################################################

def ShowBookingView(request, pk):
    a = Booking.objects.get(id = pk)

    print(a)
    return render(request, 'BookingApp/show_booking.html',{'a':a})


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