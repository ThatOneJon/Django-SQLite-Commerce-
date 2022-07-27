from django.urls import path
from . import views
import re

app_name = "Sales"

urlpatterns = [
    path("", views.index, name ="index"),
    path("listing/<Sid>/", views.listingSite, name = "listingSite"),
    path("create", views.createListing, name ="create"),
]
