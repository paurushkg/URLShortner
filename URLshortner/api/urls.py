from django.urls import path
from api import views

urlpatterns = [
    path('', views.UrlShortner.as_view()),
    #path("<str:id>", views.shorten, name="shorten")
]