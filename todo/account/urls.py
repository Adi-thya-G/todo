from django.urls import path
from .views import *
urlpatterns = [
    path('register/',registeration,name="register"),
    path("login/", login_page, name="login"),
    path("logout/",logout_page, name='logout'),
    path("",home,name="home"),
    path("create/",create_todo,name="create"),
    path("delete/<str:uid>/",delete_tod,name="delete"),
    path("edit/<str:uid>/",edit_todo,name="edit")
]
