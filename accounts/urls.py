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
         name="email_varification"),

    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="account-section/password-reset-sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account-section/password-reset-confirm.html"),
         name="password_reset_confirm"),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="account-section/password-reset-complete.html"),
         name="password_reset_complete"),
]
