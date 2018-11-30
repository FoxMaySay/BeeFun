from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from .models import GameDetail, GameSocial

def index(request):
    return render(request, 'index.html')


def gamesSum(request):
    all_game = GameDetail.objects.all()
    # 分页
    paginator = Paginator(all_game, 4)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    context = {
        'all_game': all_game,
        'contacts': contacts
    }
    return render(request, 'games.html', context)


def gameDetail(request, game_id):
    game = get_object_or_404(GameDetail, game_id=game_id)
    all_game = GameDetail.objects.all()
    game_social = GameSocial.objects.all()
    context = {
        'game': game,
        'all_game': all_game,
        'game_social': game_social,
    }
    return render(request, 'detail.html', context)


def faq(request):
    return render(request, 'faq.html')


def contactUs(request):
    return render(request, 'contact.html')


def submit(request):
    return render(request, 'submit.html')


def page404(request):
    return render(request, '404.html')
