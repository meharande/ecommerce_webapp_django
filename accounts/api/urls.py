from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from accounts.api.views import (
    register,
    user_details,
    login_view,
    logout_view
)
urlpatterns = [
    path('login/', login_view, name="login-api"),
    path('logout/', logout_view, name="logout-api"),
    path('register/', register, name="register-api"),
    path('user_details/', user_details, name="user-details"),
    # path('login/', obtain_auth_token, name="obtain_auth_token")
]
