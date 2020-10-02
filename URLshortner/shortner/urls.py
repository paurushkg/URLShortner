from django.urls import path
from shortner import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:id>", views.shorten, name="shorten")
]