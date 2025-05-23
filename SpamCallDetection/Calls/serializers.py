from rest_framework import serializers
from .models import PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'is_spam', 'owner_name','image']
