from rest_framework.serializers import ModelSerializer
from .models import MenuItem, Booking

class MenuSerializer(ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = '__all__'
    