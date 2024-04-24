from rest_framework import serializers
from .models import *

class SuvSerializer(serializers.Serializer):
    class Meta:
        model=Suv
        fields='__all__'

class MijozSerializer(serializers.Serializer):
    class Meta:
        model=Mijoz
        fields='__all__'

class AdminSerializer(serializers.Serializer):
    class Meta:
        model=Admin
        fields='__all__'

class HaydovchiSerializer(serializers.Serializer):
    class Meta:
        model=Haydovchi
        fields='__all__'

class BuyurtmaSerializer(serializers.Serializer):
    class Meta:
        model=Buyurtma
        fields='__all__'



