from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(primary_key=True, max_length=80)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True, max_length=50)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='genres', blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    links = models.TextField()
    image = models.ImageField(upload_to='authors')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cycle(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    info = models.TextField()
    image = models.ImageField(upload_to='publishers')
    birthdate = models.DateField('Date of Birth')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField(Genre, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    desc = models.TextField()
    info = models.TextField()
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='books', blank=True, null=True)
    puplisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    pubdate = models.DateField('Date of publish')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    prizes = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='books')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('book-detail', kwargs={'pk': self.pk})

    @property
    def get_genre(self):
        if self.genre:
            return self.genre.all()
        return False



