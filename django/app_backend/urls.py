from django.urls import path
from app_backend import views, views_game, tasks

urlpatterns = [
    path('user/', views.user),
    path('friends/', views.friends),
    path('search/', views.search_users),
    path('top/', views.top),    
    path('html/', views_game.getHTML),  
    #path('ghtml/', tasks.generateRandomAndupdateHTML),
    path('user-results/',views.user_results),  
    path('friends/requests',views.friend_requests),
]
