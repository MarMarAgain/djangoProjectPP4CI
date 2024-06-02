from django.urls import path

from masterworks import views

urlpatterns = [
    path("masterworks/", views.index, name="index")
]