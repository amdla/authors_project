from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('test/', views.test_view, name='test'),
]
