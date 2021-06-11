from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.post_content, name='post_content'),
    path('private/', views.post_private, name='post_private'),
]