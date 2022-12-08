from django.urls import path
from calender import views

urlpatterns = [
    path('calender/', views.CalenderList.as_view()),
    path('calender/<int:pk>/', views.CalenderDetail.as_view()),
    path('calender/<int:pk>/add_member', views.AddTaskMember.as_view()),
    path('calender/<int:pk>/remove_member', views.DeleteTaskMember.as_view()),
]
