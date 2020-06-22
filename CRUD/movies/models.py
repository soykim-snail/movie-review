from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    title_en = models.CharField(max_length=1000)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=100)
    watch_grade = models.CharField(max_length=100)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

# comments
class Comment(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    

