from django.urls import path
from . import views

urlpatterns = [
    path("grant/", views.grantToken),
    path("refresh/", views.grantToken),
]
