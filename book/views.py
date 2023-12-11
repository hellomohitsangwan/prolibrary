from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book

def homepageView(request):
    books = Book.objects.all()

    if request.GET.get('sort') == 'price':
        books = books.order_by('price')

    return render(request, "viewbook.html", {"books": books})


def addBookView(request):
    return render(request, "addbook.html")

def addBook(request):
    if request.method == "POST":
        t = request.POST["title"]
        p = request.POST["price"]
        c = request.POST["category"]  
        d = request.POST["description"]  
        book = Book(title=t, price=p, category=c, description=d)
        book.save()
        return HttpResponseRedirect('/')

def editBook(request):
    if request.method == "POST":
        book = Book.objects.get(id=request.POST['bid'])
        book.title = request.POST["title"]
        book.price = request.POST["price"]
        book.category = request.POST["category"] 
        book.description = request.POST["description"] 
        book.save()
        return HttpResponseRedirect('/')

def editBookView(request):
    book = Book.objects.get(id=request.GET['bookid'])
    return render(request, "edit-book.html", {"book": book})

def deleteBookView(request):
    book = Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')
