from django.contrib import admin
from django.urls import path,include
from .views import homepageView

urlpatterns = [
    path('', homepageView),
        path("add/",addBookView),
]
