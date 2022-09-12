from . import views
from django.urls import path
polls/urls.py¶


urlpatterns = [
    path('', views.index, name='index'),
]
˝
