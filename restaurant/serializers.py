from rest_framework.serializers import ModelSerializer
from .models import MenuItem, Booking
from django.contrib.auth.models import User

class MenuSerializer(ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = '__all__'
    
class BookingSerializer(ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'username', 'email']
        