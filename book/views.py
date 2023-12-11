from django.shortcuts import render
from django.http import HttpResponse

def homepageView(request):
    books = Book.objects.all()
    return render(request, "viewbook.html", {"books": books})

def addBookView(request):
    return render(request, "addbook.html")