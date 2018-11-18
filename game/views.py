from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def page404(request):
    return render(request, '404.html')