from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweetedit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    # user functionality
    path('register/', views.register, name='register'),
    path('tweets/search/', views.search_tweets, name='search_tweets'),
    
]
