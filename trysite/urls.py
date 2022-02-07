from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('now/',views.current_date, name="date")
]
