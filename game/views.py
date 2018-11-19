from django.shortcuts import render


def Home(request):
    return render(request, 'index.html')


def GamesSum(request):
    return render(request, 'games.html')


def GameDetail(request):
    return render(request, 'detail.html')


def FAQ(request):
    return render(request, 'faq.html')


def ContactUs(request):
    return render(request, 'contact.html')


def Submit(request):
    return render(request, 'submit.html')


def Page404(request):
    return render(request, '404.html')
