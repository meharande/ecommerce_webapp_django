from django.urls import path
from .views import (
    login_view,
    logout_view,
    registration_view,
    profile_view
)

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile")
]