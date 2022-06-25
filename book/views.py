from multiprocessing import context
from pydoc import pager
from re import I
from django.shortcuts import render, redirect
from django.urls import  reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg, Q
from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE
from django.contrib import messages
from django.views import generic





# Create your views here.

class ListBookView(LoginRequiredMixin, ListView):
    template_name = 'book/book_list.html'
    model = Book
    paginate_by = ITEM_PER_PAGE

class DetailBookView(LoginRequiredMixin, DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBookView(LoginRequiredMixin, CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title', 'text', 'category','img_url', 'thumbnail')
    success_url = reverse_lazy('list-book')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeleteBookView(LoginRequiredMixin, DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdateBookView(LoginRequiredMixin, UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ('title', 'text', 'category', 'img_url','thumbnail')
    success_url = reverse_lazy('list-book')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.id})

def index_view(request):
    object_list = Book.objects.order_by('-id')
    ranking_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')[:5]
    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    return render(request, 'book/index.html', {'ranking_list' : ranking_list, 'page_obj':page_obj})
    

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_view = 'book/review/_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.book.id})


def Search_Book(request):
    page_obj = Book.objects.order_by('-id')
    keyword = request.GET.get('keyword')
    if keyword:
        page_obj = page_obj.filter(
            Q(title__icontains=keyword)
        )
        messages.success(request, '{}の検索結果'.format(keyword))
    

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'book/book_search.html', context)

    
def Categorize_by_business(request):

    object_list = Book.objects.filter(category='business')
    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)

    context = {
        'page_obj': page_obj,
    }
    
    return render(request, 'book/categorize_by_category.html' ,context)
    

def Categorize_by_science_and_Technology(request):
    
    object_list = Book.objects.filter(category='science ・Technology')
    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    context = {
        'page_obj':page_obj,
    }
    
    return render(request, 'book/categorize_by_category.html' ,context)

def Categorize_by_Humanities_and_ideas(request):
    
    object_list = Book.objects.filter(category='Humanities・ideas')
    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    context = {
        'page_obj':page_obj,
    }
    
    return render(request, 'book/categorize_by_category.html' ,context)

def Categorize_by_computer_and_IT(request):
    
    object_list = Book.objects.filter(category='computer・IT')
    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    context = {
        'page_obj':page_obj,
    }
    
    return render(request, 'book/categorize_by_category.html' ,context)


def Categorize_by_assesment(request):
    
    object_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    context = {
        'page_obj':page_obj,
    }
    
    return render(request, 'book/categorize_by_category.html' ,context)