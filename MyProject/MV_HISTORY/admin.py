from django.contrib import admin
from .models import Article, Author, Task

admin.site.register([Article, Author, Task])
# Register your models here.
