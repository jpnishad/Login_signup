from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.loginform, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('password/', views.pass_change, name='password'),
]
