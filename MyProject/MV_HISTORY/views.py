from django.shortcuts import render
import os
from .models import Article
base_info = [
    {
        'id': 1,
        'title': 'ФАКИ',
        'text': 'Кто чемпион?',
        'img': 'MV_HISTORY/images/fakt.png',
    },
    {
        'id': 2,
        'title': 'ФИВТ',
        'text': 'Слышно нам на всю Долгопу!',
        'img': 'MV_HISTORY/images/fpmi.png',
    },
{
        'id': 3,
        'title': 'ФУПМ',
        'text': 'ФУПМ - !',
        'img': 'MV_HISTORY/images/fpmi.png',
    },
    {
        'id': 4,
        'title': 'ЛФИ',
        'text': 'За Ландау!',
        'img': 'MV_HISTORY/images/lfi.png',
    },
    {
        'id': 5,
        'title': 'ФРКТ',
        'text': 'От коробки до НК, лучше всех!',
        'img': 'MV_HISTORY/images/frkt.png',
    },
    {
        'id': 6,
        'title': 'ФЭФМ',
        'text': 'Мы болеем за кванты, потому что мы кванты!',
        'img': 'MV_HISTORY/images/fefm.png',
    },
    {
        'id': 7,
        'title': 'ФБМФ',
        'text': 'Мы болеем за БМ, потому что мы с проблем!',
        'img': 'MV_HISTORY/images/bfmf.png',
    },
    {
        'id': 8,
        'title': 'ИНБИКСТ',
        'text': 'ИНБИКСТ ИНБИКСТ ИНБИКСТ',
        'img': 'MV_HISTORY/images/fnbit.png',
    },
    {
        'id': 9,
        'title': 'ФАЛТ',
        'text': 'На реактивной тяге!',
        'img': 'MV_HISTORY/images/fakt.png',
    },
]

departments = {}  # пустой словарь
departments["1"] = 'ФАКИ'
departments["2"] = 'ФИВТ'
departments["3"] = 'ФУПМ'
departments["4"] = 'ЛФИ'
departments["5"] = 'ФРКТ'
departments["6"] = 'ФЭФМ'
departments["7"] = 'ФБМВ'
departments["8"] = 'ИНБИКСТ'
departments["9"] = 'ФАЛТ'

def index(request):
    return render(request, 'MV_HISTORY/dep_list.html', {'base_infos': base_info})

def get_article(request, info_article_id):
    depart = departments[f"{info_article_id}"]
    info = Article.objects.filter(title__contains=depart).values()
    return render(request, 'MV_HISTORY/dep_article.html',  {'info_article': info})

def get_task(request, task_number):
    info = Article.objects.filter(id = task_number).values()
    return render(request, 'MV_HISTORY/task.html',  {'task_info': info})