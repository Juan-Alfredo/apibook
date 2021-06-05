from catalogo.models import Author
from catalogo.models import Book
from catalogo.forms import ModelBookForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView


class Author_list(ListView):
    model = Author
    fields = '__all__'

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

def update_book(request, pk):
    if request.method == 'POST':
        
        data = request.POST

        author = Author.objects.get(pk=data['author'])

        book = Book.objects.get(pk=pk)
        book.title = data['title']
        book.author = author
        book.editorial = data['editorial']
        book.year = data['year']
        book.volume = data['volume']
        book.save()

        return redirect('/catalog')

    else:
        book = Book.objects.get(pk=pk)
        form = ModelBookForm(book.__dict__)
        return render(request, 'catalogo/new.html', {"form": form})


def new_book(request):
    if request.method == 'POST':
        data = request.POST

        book = Book()
        book.title = data['title']
        #book.autor = data['autor']
        book.editorial = data['editorial']
        book.year = data['year']
        book.volumen = data['volume']
        book.save()

        return redirect('/catalog')
        
    else:
        form = ModelBookForm()
        return render(request, 'catalogo/new.html', {"form": form})

def get_books_by_editorial(request, editorial):
    books = Book.objects.filter(editorial=editorial)
    year = request.GET.get("year")
    
    if year != None:
        books = books.filter(year=year)

    return render(request, 'catalogo/index.html', {'books': books})

# Create your views here.
def catalog_list(request):
    books = Book.objects.all()
    return render(request, 'catalogo/index.html', {'books': books})