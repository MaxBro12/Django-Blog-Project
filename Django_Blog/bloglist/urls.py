from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_list),
    path('create/', views.create_new),
]
