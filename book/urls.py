
from django.contrib import admin
from django.urls import path,include,re_path
from .views import homepageView,addBookView,addBook,editBook,editBookView,deleteBookView

urlpatterns = [
    path("",homepageView),
    path("add/",addBookView),
    path("add/add",addBook),
    path("edit/",editBookView),
    path("edit/edit",editBook),
    path("delete",deleteBookView)
]
