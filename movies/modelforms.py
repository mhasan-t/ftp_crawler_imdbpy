from django import forms

from movies.models import Movies


class CreateMoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('name', 'year', 'genre', 'photo', 'cast', 'plot', 'synopsis', 'video')


# class Auto(forms.Form):
#     description = forms.CharField()

class CreateFromVideo(forms.Form):
    name = forms.CharField(max_length=1000)
    video = forms.CharField(max_length=9999)