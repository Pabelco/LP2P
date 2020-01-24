from django.urls import path
from . import views

urlpatterns = [
    path('trashes', views.get_trashes, name='LocateTrash'),
]