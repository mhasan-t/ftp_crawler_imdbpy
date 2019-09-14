from django.db import models
from etc_files.movie_types import TYPES, IND


class Movies(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField()
    type = models.CharField(choices=TYPES, max_length=10)
    industry = models.CharField(choices=IND, max_length=3)
    photo = models.ImageField(upload_to='movie_photos', max_length=1000)
    video = models.CharField(max_length=1000, help_text="Put the link to your movie file")

    def __str__(self):
        return '{name}'.format(name=self.name)