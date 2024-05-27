from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class mybook(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    description = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
