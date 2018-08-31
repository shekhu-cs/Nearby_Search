from django.urls import path
from  . import views

urlpatterns = [
    path(r'restauranst/', views.NearRest.as_view()),
]