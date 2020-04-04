from django.db import models

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.tittle
