from django.urls import path

from . import views

app_name = "foods"

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("food-list/", views.foodList, name="food-list"),
    path("food-detail/<str:pk>/", views.foodDetail, name="food-detail"),
    path("food-create/", views.foodCreate, name="food-create"),
    path("food-update/<str:pk>/", views.foodUpdate, name="food-update"),
    path("food-delete/<str:pk>/", views.foodDelete, name="food-delete"),
    path("image-list/", views.imageList, name="image-list"),
    path("image-detail/<str:pk>/", views.imageDetail, name="image-detail"),
    path("image-create/", views.imageCreate, name="image-create"),
    path("image-update/<str:pk>/", views.imageUpdate, name="image-update"),
    path("image-delete/<str:pk>/", views.imageDelete, name="image-delete"),
]
