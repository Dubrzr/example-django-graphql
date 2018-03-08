from graphene_django import DjangoObjectType
import graphene

from articles.models import Article as ArticleModel, Author as AuthorModel


class Article(DjangoObjectType):
    class Meta:
        model = ArticleModel

class Author(DjangoObjectType):
    class Meta:
        model = AuthorModel

class Query(graphene.ObjectType):
    articles = graphene.List(Article)
    authors = graphene.List(Author)

    def resolve_articles(self, info):
        return ArticleModel.objects.all()

    def resolve_authors(self, info):
        return AuthorModel.objects.all()


schema = graphene.Schema(query=Query)
