from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('games/', views.GamesSum, name='games'),
    path('<slug>', views.GameDetail, name='detail'),
    path('faq/', views.FAQ, name='faq'),
    path('contact-us/', views.ContactUs, name='contact-us'),
    path('submit/', views.Submit, name='submit'),
    path('404/', views.Page404, name='404'),
]
