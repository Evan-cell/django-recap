from django.urls import path
from . import views

urlpatterns = [
    path('now/',views.current_date, name="date"),
    path('', views.welcome, name="welcome")
]
