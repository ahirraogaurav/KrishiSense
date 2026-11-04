from django.contrib.auth import views as auth
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth.LoginView.as_view(template_name="advisor/auth_form.html", authentication_form=LoginForm,
         redirect_authenticated_user=True,
         extra_context={"title": "Log in", "button": "Log in", "alt": "signup", "alt_text": "New here? Create an account"}), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("password/", views.PasswordChange.as_view(), name="password_change"),
    path("predict/", views.predict, name="predict"),
    path("result/<int:pk>/", views.result, name="result"),
    path("history/", views.history, name="history"),
    path("history/<int:pk>/delete/", views.delete_prediction, name="delete_prediction"),
    path("crops/", views.crop_list, name="crops"),
    path("crops/<slug:key>/", views.crop_detail, name="crop_detail"),
]
