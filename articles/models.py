from email.policy import default
from django.db import models
from matplotlib import image
from matplotlib.pyplot import title

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField()
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(default='default.jpg' , blank = True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'