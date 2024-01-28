from django.urls import path
from .views import login, SignUp

urlpatterns = [
    path("login", login, name="login"),
    path('register', SignUp.as_view(), name="register"),
    path("logout", login , name="logout"),

]
