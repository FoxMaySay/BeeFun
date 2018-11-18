from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('404/', views.page404, name='404')
]
