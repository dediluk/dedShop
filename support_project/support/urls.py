from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

app_name = 'support'

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login', LoginAPIView.as_view()),

]
