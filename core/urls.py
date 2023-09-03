from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import messages

from . import views

urlpatterns = [

    path('', views.home, name="home"),

    # Rutas para listar elementos
    path('movies/', views.movie_list, name='movie_list'),
    path('series/', views.series_list, name='series_list'),
    path('books/', views.book_list, name='book_list'),
    path('comics/', views.comic_list, name='comic_list'),

    # Rutas para ver detalles de elementos
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('series/<int:pk>/', views.series_detail, name='series_detail'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('comics/<int:pk>/', views.comic_detail, name='comic_detail'),

    # Rutas para crear elementos
    path('movies/create/', views.movie_create, name='movie_create'),
    path('series/create/', views.series_create, name='series_create'),
    path('books/create/', views.book_create, name='book_create'),
    path('comics/create/', views.comic_create, name='comic_create'),

    # Rutas para actualizar elementos
    path('movies/<int:pk>/update/', views.movie_update, name='movie_update'),
    path('series/<int:pk>/update/', views.series_update, name='series_update'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('comics/<int:pk>/update/', views.comic_update, name='comic_update'),

    # Rutas para eliminar elementos
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('series/<int:pk>/delete/', views.series_delete, name='series_delete'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('comics/<int:pk>/delete/', views.comic_delete, name='comic_delete'),
    path('movie_search/', views.movie_search, name='movie_search'),

    # Registro:

    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # About:
    path('about/', views.about, name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
