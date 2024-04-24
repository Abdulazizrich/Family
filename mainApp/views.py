from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,filters
from .serializers import *
from .models import *

class MyCustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100
class SuvViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = MijozSerializer

class MijozViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['ism', 'tel']
    pagination_class = MyCustomPagination


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class HaydovchiViewSet(ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer

class BuyurtmaViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer



