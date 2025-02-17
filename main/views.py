from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib import messages

from .models import *
from .forms import *


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class MainPageViews(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

    def get_template_names(self):
        template_name = super(MainPageViews, self).get_template_names()
        search = self.request.GET.get('q')
        if search:
            template_name = 'search.html'
        return template_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        if search:
            context['books'] = Book.objects.filter(Q(title__icontains=search)|
                                                   Q(desc__icontains=search))
        else:
            context['books'] = Book.objects.all()
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(category=self.slug)

        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'category-detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()

        return context



class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre-detail.html'
    context_object_name = 'genre'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(genre=self.slug)

        return context

def genre(request):
    genre = Genre.objects.all()
    return render(request, 'genre.html', locals())



def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save()
            return redirect(book.get_absolute_url())
    else:
        book_form = BookForm()
    return render(request, 'add-book.html', locals())

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_form = BookForm(request.POST or None, instance=book)

    if book_form.is_valid():
        book = book_form.save()
        return redirect(book.get_absolute_url())

    return render(request, 'update-book.html', locals())


class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete-book.html'
    success_url = reverse_lazy('index')
    context_object_name = 'book'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Успешно удалено!')
        return HttpResponseRedirect(success_url)


class AuthorView(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.slug)

        return context