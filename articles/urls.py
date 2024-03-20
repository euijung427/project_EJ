
from django.urls import path
from articles import views

urlpatterns = [
    path('students/<int:student_id>/', views.student_detail)
]
