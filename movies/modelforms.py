from django import forms

from movies.models import Movies


class CreateMoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('name', 'year', 'genre', 'photo', 'cast', 'plot', 'synopsis', 'video')


class Auto(forms.Form):
    description = forms.CharField()