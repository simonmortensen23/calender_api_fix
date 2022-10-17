from django.urls import path
from posts import views

urlpatterns = [
    path('calender/', views.CalenderList.as_view()),
    path('calender/<int:pk>/', views.CalenderDetail.as_view()),
]