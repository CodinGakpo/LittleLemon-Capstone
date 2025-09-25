from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .models import Menu
from .serializers import MenuSerializer
# Create your views here.


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(DestroyAPIView,RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer