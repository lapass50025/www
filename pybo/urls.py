from django.urls import path, include
from pybo import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='pybo_index'),
    path('<int:question_id>/', views.detail, name='pybo_detail'),
    path('reply/<int:question_id>/', views.reply, name='pybo_reply'),
    path('write/', views.write, name='pybo_write'),
    path('modify/<int:question_id>/', views.modify, name='pybo_modify'),
    path('delete/<int:question_id>/', views.delete, name='pybo_delete'),
]
