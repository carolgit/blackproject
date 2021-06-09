from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_content, name='post_content'),
]