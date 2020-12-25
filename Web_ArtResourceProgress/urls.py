from django.urls import path
from . import views

app_name = 'Web_ArtResourceProgress'

urlpatterns = [
    path('', views.IndexView, name = 'index'),
    path('detail', views.Detailds)
]