from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .models import Menu,Booking
from .serializers import MenuSerializer,BookSerializer
# Create your views here.


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(DestroyAPIView,RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer