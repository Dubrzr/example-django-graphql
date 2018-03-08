from django.db import models
import datetime

class Author(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    created_at = models.DateField(default=datetime.date.today)

    @property
    def get_name(self):
        return self.firstname + ' ' + self.lastname

class Article(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=250)
    created_at = models.DateField(default=datetime.date.today)
    deleted_at = models.DateField(null=True)
    author = models.ForeignKey(to=Author, on_delete=None)