from django.db import models
from django.contrib.auth.models import User


#Note model for creating and storing user notes to the database
class Note(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # author field is a forieng key to an existing user instance
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    # we print the title of the note when get it from the db
    def __str__(self):
        return self.title


    # return the first 50 characters in the body
    def snippet(self):
        return self.body[:50] + "..."
