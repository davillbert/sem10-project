from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:info_article_id>/', views.get_article, name='info_article_id'),
    path('tasks/', views.tasks, name='tasks') , # Обновленный путь для страницы tasks_list.html
    path('quiz/', views.quiz_view, name='quiz'),

path('new/', views.new_tasks, name='new_tasks')
]
