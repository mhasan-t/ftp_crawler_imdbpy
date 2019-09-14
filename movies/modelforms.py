from django import forms

from movies.models import Movies


class CreateMoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('name', 'year', 'type', 'industry', 'photo', 'video')