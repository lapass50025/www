from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='common_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='common_logout'),

    path('signup/', views.signup, name='common_signup'),
]
