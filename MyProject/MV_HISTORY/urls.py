from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('<int:info_article_id>/', views.get_article, name='info_article_id'),]
