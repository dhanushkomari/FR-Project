from django.contrib import admin
from .models import Department, Doctor, Booking

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at']
    list_per_page = 20

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','department', 'designation', 'contact', 'email', 'created_at',]
    list_per_page = 20

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','patient','doctor', 'Booking_time', 'created_at')
    list_per_page = 20

admin.site.register(Booking, BookingAdmin)


admin.site.register(Department,DepartmentAdmin)
admin.site.register(Doctor,DoctorAdmin)

