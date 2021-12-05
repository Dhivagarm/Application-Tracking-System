from django.urls import path

from . import views

urlpatterns = [
    path("register",views.register,name="register"),
    path("register2",views.register2,name="register2"),
    path("login",views.login,name="login"),
    path("login2",views.login2,name="login2"),
    path("logout",views.logout,name="logout")
]