
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.Signup, name="signup"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('quiz/',views.quiz),
    path('question/',views.addQuestion),
]