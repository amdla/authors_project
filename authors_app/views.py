from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import AuthorForm
from .models import Author


def home(request):
    return render(request, 'authors_app/home.html')


def test_view(request):
    return HttpResponse("This is a test view.")


class AuthorListView(ListView):
    model = Author
    template_name = 'authors_app/forms/author_list.html'
    context_object_name = 'authors'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors_app/forms/author_form.html'
    success_url = reverse_lazy('author-list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors_app/forms/author_form.html'
    success_url = reverse_lazy('author-list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors_app/forms/author_confirm_delete.html'
    success_url = reverse_lazy('author-list')
