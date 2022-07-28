from django.urls import path
from . import views
import re

app_name = "Sales"

urlpatterns = [
    path("", views.index, name ="index"),
    path("categories/", views.cat, name = "cat"),
    path("categories/<categ>", views.catDetail, name = "catDetail"),
    path("create", views.createListing, name ="create"),
    path("listing/<Sid>/", views.listingSite, name = "listingSite"),

]
