from django.urls import path

from . import views

app_name = 'workspace'
urlpatterns = [
    path('', views.index, name='index'),
]