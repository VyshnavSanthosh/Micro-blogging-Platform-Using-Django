from . import views
from django.urls import path


urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name='edit_tweet'),
    path('register/', views.userRegisteration, name='registeration'),
    path('logout/', views.logout_view, name='logout'),
]