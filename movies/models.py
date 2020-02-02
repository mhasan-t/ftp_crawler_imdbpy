from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='movie_photos', max_length=1000, blank=True, null=True)
    cast = models.CharField(max_length=9999)
    plot = models.CharField(max_length=9999)
    synopsis = models.CharField(max_length=999999)
    video = models.CharField(max_length=1000, help_text="Put the link to your movie file", blank=True, null=True)
    imdb_found = models.BooleanField(default=False, blank=True, null=True)
    manual = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=4, null=True)
    imdbid = models.CharField(max_length=20, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

