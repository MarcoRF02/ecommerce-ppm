from django.urls import path
from .views import SignUpView, MyLoginView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='store:home'), name="logout"),
]
