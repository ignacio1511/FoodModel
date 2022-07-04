from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Food, FoodImageURL
from .serializers import FoodImageURLSerializer, FoodSerializer


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "FoodList": "/food-list/",
        "FoodDetailView": "/food-detail/<str:pk>/",
        "FoodCreate": "/food-create/",
        "FoodUpdate": "/food-update/<str:pk>/",
        "FoodDelete": "/food-delete/<str:pk>/",
        "ImageList": "/image-list/",
        "ImageDetailView": "/image-detail/<str:pk>/",
        "ImageCreate": "/image-create/",
        "ImageUpdate": "/image-update/<str:pk>/",
        "ImageDelete": "/image-delete/<str:pk>/",
    }

    return Response(api_urls)


# Foods


@api_view(["GET"])
def foodList(request):
    foods = Food.objects.all().order_by("-id")
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def foodDetail(request, pk):
    foods = Food.objects.get(id=pk)
    serializer = FoodSerializer(foods, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def foodCreate(request):
    serializer = FoodSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def foodUpdate(request, pk):
    new_food = Food.objects.get(id=pk)
    serializer = FoodSerializer(instance=new_food, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def foodDelete(request, pk):
    new_food = Food.objects.get(id=pk)
    new_food.delete()

    return Response("Food succsesfully deleted!")


# Images


@api_view(["GET"])
def imageList(request):
    images = FoodImageURL.objects.all().order_by("-id")
    serializer = FoodImageURLSerializer(images, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def imageDetail(request, pk):
    images = FoodImageURL.objects.get(id=pk)
    serializer = FoodImageURLSerializer(images, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def imageCreate(request):
    serializer = FoodImageURLSerializer(data=request.data)

    print(serializer)

    if serializer.is_valid():
        serializer.save()
        print("SERIALIZER DATA ... ", serializer.data)

    return Response(serializer.data)


@api_view(["POST"])
def imageUpdate(request, pk):
    new_food = FoodImageURL.objects.get(id=pk)
    serializer = FoodImageURLSerializer(instance=new_food, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def imageDelete(request, pk):
    new_food = FoodImageURL.objects.get(id=pk)
    new_food.delete()

    return Response("FoodImageURL succsesfully deleted!")
