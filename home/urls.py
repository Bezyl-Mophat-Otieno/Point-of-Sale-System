from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
path('dashboard/', views.index,name='index'),
path('about/', views.aboutPage,name='about'),

]