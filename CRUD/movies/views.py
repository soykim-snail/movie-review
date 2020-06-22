from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comment_set.all()
    form = CommentForm()
    context = {
        'movie': movie,
        'comments': comments,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid:
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

# deleting comment ... only POST
@require_POST
def comment_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)

# creating comment ... movie_pk is specified
@require_POST
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # content = request.POST.get('content')
    # Comment.objects.create(content=content, movie=movie)
    form = CommentForm(request.POST)
    print(form) # html 문서임을 확인할 수 있다.
    # <tr><th><label for="id_content">Content:</label></th><td>
    # <textarea name="content" cols="40" rows="10" required id="id_content">
    # 111</textarea></td></tr>
    if form.is_valid():
        comment = form.save(commit=False)     
        comment.movie = movie
        comment.save()
    return redirect('movies:detail', movie_pk)
    

