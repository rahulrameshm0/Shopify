from django.urls import path
from . import views
urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register"),
    # path('password_reset/', views.password_reset, name="password_reset"),
    path('email_varification/', views.email_verification, name="email_verification"),
]
