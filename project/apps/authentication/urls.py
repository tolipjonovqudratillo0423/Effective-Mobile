from django.urls import path

from apps.authentication.views import (
    RegisterAPIView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
]