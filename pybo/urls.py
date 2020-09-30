from django.urls import path, include
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='pybo_index'),
]
