from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register"),
    path('', views.dashboard, name="dashboard"),

    # password  reset
    path('email_varification/',
         auth_views.PasswordResetView.as_view(template_name="account-section/email-varification.html"),
         name="email_verification"),

    path('password_reset_sent/', auth_views.PasswordResetView.as_view(), name="password_reset_sent"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetView.as_view(), name="password_reset_complete"),
]
