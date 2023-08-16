from django.urls import  path
from library_app import views  # Correct import


urlpatterns = [
    path('', views.get_meals, name = "get_meals"),
    path('meals/<int:id>/',views.meal_detail, name = "meal_detail")
]