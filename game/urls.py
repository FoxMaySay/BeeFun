from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.gamesSum, name='games'),
    path('game/<slug:slug_name>', views.gameDetail, name='detail'),
    path('faq/', views.faq, name='faq'),
    path('contact-us/', views.contactUs, name='contact-us'),
    path('submit/', views.submit, name='submit'),
    path('404/', views.page404, name='404'),
]

