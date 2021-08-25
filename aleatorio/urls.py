from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index.html', views.random_word),
    path('index.html/reset', views.reset)
]
