from django.urls import path
from .views import (
    StudentListView, StudentCreateView,
    StudentUpdateView, StudentDeleteView, StudentDetailView
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('add/', StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]