from django.urls import path

from articles.views import article, create_article, create_author, login_user

articles_urls = [
    path('articles/<int:year>/', article),
    path('create_article', create_article, name='create_article'),
    path('create_author', create_author, name='create_author'),
    path('login', login_user, name='login'),
]