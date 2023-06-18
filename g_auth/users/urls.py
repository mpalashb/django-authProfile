from django.urls import path
from users.views import (
    HomePage, ProfileDash,ProfileDelete, CreateProfile, UserRegisterView,
)

app_name = 'users'

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('create-profile', CreateProfile.as_view(), name='create-profile'),
    path('profile-del', ProfileDelete.as_view(), name='del-profile'),
    path('profile-dash', ProfileDash.as_view(), name='dash'),
    path('', HomePage.as_view(), name='home'),
]