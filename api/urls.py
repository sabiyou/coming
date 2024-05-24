from django.urls import path
from . import views as v
from rest_framework.authtoken import views

app_name = "api"

urlpatterns = [
    path('login', v.LoginView.as_view(), name='login'),
    path('emails', v.EmailView.as_view(), name='emails'),
    path('token/', views.obtain_auth_token)
]







