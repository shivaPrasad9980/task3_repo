from django.urls import path
from .views import register, login_view, logout_view, profile, activate_account

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
]
