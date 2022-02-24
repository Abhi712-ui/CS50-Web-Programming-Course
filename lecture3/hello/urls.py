from unicodedata import name
from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="index"),
    path("abhi", views.abhi, name="abhi"),
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet")

]