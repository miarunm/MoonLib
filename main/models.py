from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(primary_key=True, max_length=80)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True, max_length=50)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    links = models.TextField()
    image = models.ImageField(upload_to='authors')


class Cycle(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    info = models.TextField()
    image = models.ImageField(upload_to='publishers')
    birthdate = models.DateField('Date of Birth')


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField(Genre)
    category = models.ManyToManyField(Category)
    desc = models.TextField()
    info = models.TextField()
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='books')
    puplisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    pubdate = models.DateField('Date of publish')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    quote = models.TextField()
    prizes = models.TextField()
