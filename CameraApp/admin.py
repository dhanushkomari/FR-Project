from django.contrib import admin
from .models import Status, Patient

# Register your models here.

admin.site.site_header = 'Hyderabad Smiles'

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']
    list_per_page = 20

admin.site.register(Status, StatusAdmin)

class PatientAdminn(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name', 'blood_group', 'gender', 'contact', 'email', 'city', 'created_at']

admin.site.register(Patient, PatientAdminn)

