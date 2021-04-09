from rest_framework import serializers 
from .models import Patient, Status


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'