from rest_framework import serializers
from .models import Furniture, Rooms


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class FurnitureSerializer(serializers.ModelSerializer):
    room = RoomsSerializer()
    class Meta:
        model = Furniture
        fields = '__all__'