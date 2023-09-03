from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from .models import Movie, Series, Book, Comic, CustomUser

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_year',]

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['title', 'description', 'release_year',]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'release_year',]

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'description', 'release_year',]

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email',]

class ChangePasswordForm(PasswordChangeForm):
    pass