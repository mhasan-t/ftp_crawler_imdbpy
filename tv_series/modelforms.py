from django import forms

from tv_series.models import TV


class CreateTvsForm(forms.ModelForm):
    class Meta:
        model = TV
        fields = ('name', 'year', 'genre', 'photo', 'cast', 'plot', 'synopsis', 'dir', 'imdbid')

class CreateFromVideo(forms.Form):
    name = forms.CharField(max_length=1000)
    dir = forms.CharField(max_length=9999)