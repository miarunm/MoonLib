from main.models import Genre, Category


def get_genres(request):
    genres = Genre.objects.filter(parent__isnull=True)
    return {'genres': genres}

def get_category(request):
    categories = Category.objects.all()
    return {'categories': categories}