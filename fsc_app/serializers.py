# fsc_app/serializers.py
from rest_framework import serializers
from .models import StripingForm, UserProfile  # Update the import to include UserProfile

class StripingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripingForm  # Update to use the correct model
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile  # Use the correct model name
        fields = '__all__'
