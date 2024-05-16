from django.shortcuts import render
import os

articles = [
    {
        'id': 1,
        'title': 'ФАКТ',
        'text': 'Кто чемпион?',
        'img': 'MV_HISTORY/images/fakt.png',
    },
    {
        'id': 2,
        'title': 'ФПМИ',
        'text': 'Вперёд, ФУПМы!',
        'img': 'MV_HISTORY/images/fpmi.png',
    },
    {
        'id': 3,
        'title': 'ЛФИ',
        'text': 'За Ландау!',
        'img': 'MV_HISTORY/images/lfi.png',
    },
    {
        'id': 4,
        'title': 'ФРКТ',
        'text': 'От коробки до НК, лучше всех!',
        'img': 'MV_HISTORY/images/frkt.png',
    },
    {
        'id': 5,
        'title': 'ФЭФМ',
        'text': 'Мы болеем за кванты, потому что мы кванты!',
        'img': 'MV_HISTORY/images/fefm.png',
    },
    {
        'id': 6,
        'title': 'ФБМФ',
        'text': 'Мы болеем за БМ, потому что мы с проблем!',
        'img': 'MV_HISTORY/images/bfmf.png',
    },
    {
        'id': 7,
        'title': 'ИНБИКСТ',
        'text': 'ИНБИКСТ ИНБИКСТ ИНБИКСТ',
        'img': 'MV_HISTORY/images/fnbit.png',
    }]


def index(request):
    return render(request, 'MV_HISTORY/dep_list.html', {'articles': articles})

def get_article(request, article_id):
    return render(request, 'MV_HISTORY/dep_article.html', {'article': articles[article_id - 1]})