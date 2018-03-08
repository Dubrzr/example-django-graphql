from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from articles.models import Author, Article


def fun():
    print('lol')

def article(request, year):
    #TODO debug request

    context = {
        'year': year,
        'authors': Author.objects.all(),
        'articles': Article.objects.all()
    }

    return render(
        request,
        'articles/article.html',
        context
    )

    # L'équivalent de render c'est :
    # content = loader.render_to_string('articles/article.html', context, request, using=None)
    # return HttpResponse(content, None, None)


def create_article(request):
    params = request.POST

    number = params.get('number')
    name = params.get('name')
    firstname, lastname = params.get('author').split(' ')

    author = get_object_or_404(Author, firstname=firstname, lastname=lastname)

    new_article = Article()
    new_article.author = author
    new_article.name = name
    new_article.number = number
    new_article.save()

    return article(request, 42)

def create_author(request):
    params = request.POST
    firstname = params.get('firstname')
    lastname = params.get('lastname')

    new_author = Author()
    new_author.firstname = firstname
    new_author.lastname = lastname
    new_author.save()

    return article(request, 42)

def login_user(request):
    params = request.POST

    username = params.get('username')
    password = params.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        print('User authenticated')
        login(request, user)
    else:
        print('Fail auth')

    return render(
        request,
        'login.html'
    )