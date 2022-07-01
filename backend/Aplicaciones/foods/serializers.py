from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Food, FoodImageURL


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImageURL
        fields = "__all__"
