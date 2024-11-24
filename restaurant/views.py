from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import MenuSerializer, BookingSerializer
from .models import MenuItem, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = MenuItem.objects.all()

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = MenuItem.objects.all()
    
class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    