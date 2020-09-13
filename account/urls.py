from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginview, name='loginview'),
    path('logout', views.logoutview, name="logoutview"),
    path('register', views.registerview, name='registerview'),
]