from django.db import models
from django.utils import timezone
import uuid

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __unicode__(self):
        return self.name
    def __str__(self):
        return '{}'.format(self.name)

class Article(models.Model):
    title = models.CharField(max_length=150)
    Department1 = models.CharField(max_length=150)
    Department2 = models.CharField(max_length=150)
    ScoreDepartment1 = models.IntegerField()
    ScoreDepartment2 = models.IntegerField()
    Year = models.IntegerField()
    Holidays = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
# Create your models here.
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def remove(self):
        self.delete()


    def __str__(self):
        return '{} {}'.format(self.title, self.created_date)


class Task(models.Model):
    title = models.CharField(max_length=150)
    quest = models.CharField(max_length=550)
    v1 = models.CharField(max_length=150)
    v2 = models.CharField(max_length=150)
    v3 = models.CharField(max_length=150)
    v5 = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
# Create your models here.
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def remove(self):
        self.delete()


    def __str__(self):
        return '{} {}'.format(self.title, self.created_date)


