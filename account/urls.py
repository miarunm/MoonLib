from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('main.urls')),
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile')
]