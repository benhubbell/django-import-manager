from django.contrib.auth import views as auth_views
from django.urls import path
from core.views import (
    signup,
    user_management
)


from core.views import logout

auth_urls = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('user-management', user_management, name='user_management'),
    path('signup', signup, name='signup')
]
