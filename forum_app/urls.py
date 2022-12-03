from django.urls import path
from . import views

app_name = 'forum_app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create_post/', views.create_post, name = 'create_post'),
    path('post/<int:pk>/', views.post, name = 'post'),
    path('account/<int:pk>/', views.account, name = 'account'),
    
]
