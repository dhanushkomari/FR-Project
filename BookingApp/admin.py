from django.contrib import admin
from .models import Department, Doctor, Booking, Payment

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at']
    list_per_page = 20

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','department', 'designation', 'contact', 'email', 'created_at',]
    list_per_page = 20

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','patient','doctor', 'Booking_time', 'created_at','amount', 'payment_status')
    list_per_page = 20

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_id','user', 'amount', 'created_at', 'paid')
    read_only_fields = ('id', 'payment_id','user', 'amount', 'created_at', 'paid')
    list_per_page = 20
    search_fields = ('id', 'payment_id','user')
    can_delete = False


admin.site.register(Booking, BookingAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Payment, PaymentAdmin)

