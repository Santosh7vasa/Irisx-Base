from djongo import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

#post is a table here, represented as a class. Each variable is a column in the table.
#an object of the class post can be added to the table as a row.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Reading(models.Model):
    reading1 = models.IntegerField()

class Device(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField()
    power_reading = models.ArrayField(model_container=int)

    def __str__(self):
        return self.title
