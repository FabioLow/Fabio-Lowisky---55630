from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Movie, Series, Book, Comic
from .forms import MovieForm, SeriesForm, BookForm, ComicForm, UserRegistrationForm, UserProfileForm, ChangePasswordForm
from django.views.decorators.csrf import csrf_protect

# Vistas para listar elementos de cada modelo
def home(request):
    return render(request, 'core/home.html')

@login_required
def movie_list(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'core/movie_list.html', {'movies': movies})

@login_required
def series_list(request):
    query = request.GET.get('q')
    if query:
        series = Series.objects.filter(title__icontains=query)
    else:
        series = Series.objects.all()
    return render(request, 'core/series_list.html', {'series': series})

@login_required
def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

@login_required
def comic_list(request):
    query = request.GET.get('q')
    if query:
        comics = Comic.objects.filter(title__icontains=query)
    else:
        comics = Comic.objects.all()
    return render(request, 'core/comic_list.html', {'comics': comics})

# Vistas para ver detalles de un elemento de cada modelo
@login_required
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'core/movie_detail.html', {'movie': movie})

@login_required
def series_detail(request, pk):
    series = get_object_or_404(Series, pk=pk)
    return render(request, 'core/series_detail.html', {'series': series})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

@login_required
def comic_detail(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    return render(request, 'core/comic_detail.html', {'comic': comic})

# Vistas para crear elementos de cada modelo
@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'core/movie_form.html', {'form': form})

@login_required
def series_create(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST)
        if form.is_valid():
            series = form.save()
            return redirect('series_detail', pk=series.pk)
    else:
        form = SeriesForm()
    return render(request, 'core/series_form.html', {'form': form})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'core/book_form.html', {'form': form})

@login_required
def comic_create(request):
    if request.method == 'POST':
        form = ComicForm(request.POST)
        if form.is_valid():
            comic = form.save()
            return redirect('comic_detail', pk=comic.pk)
    else:
        form = ComicForm()
    return render(request, 'core/comic_form.html', {'form': form})

# Vistas para actualizar elementos de cada modelo
@login_required
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'core/movie_form.html', {'form': form})

@login_required
def series_update(request, pk):
    series = get_object_or_404(Series, pk=pk)
    if request.method == 'POST':
        form = SeriesForm(request.POST, instance=series)
        if form.is_valid():
            series = form.save()
            return redirect('series_detail', pk=series.pk)
    else:
        form = SeriesForm(instance=series)
    return render(request, 'core/series_form.html', {'form': form})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'core/book_form.html', {'form': form})

@login_required
def comic_update(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    if request.method == 'POST':
        form = ComicForm(request.POST, instance=comic)
        if form.is_valid():
            comic = form.save()
            return redirect('comic_detail', pk=comic.pk)
    else:
        form = ComicForm(instance=comic)
    return render(request, 'core/comic_form.html', {'form': form})

# Vistas para eliminar elementos de cada modelo
@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'core/movie_confirm_delete.html', {'movie': movie})

@login_required
def series_delete(request, pk):
    series = get_object_or_404(Series, pk=pk)
    if request.method == 'POST':
        series.delete()
        return redirect('series_list')
    return render(request, 'core/series_confirm_delete.html', {'series': series})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'core/book_confirm_delete.html', {'book': book})

@login_required
def comic_delete(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    if request.method == 'POST':
        comic.delete()
        return redirect('comic_list')
    return render(request, 'core/comic_confirm_delete.html', {'comic': comic})


# Registro

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid form submission. Please correct the errors.')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home') 
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def about(request):
    return render(request, 'core/about.html')

def movie_search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()

    return render(request, 'movie_list.html', {'movies': movies})
