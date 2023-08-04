from django.urls import path

from account import views

urlpatterns = [
    path('registration',views.registration, name="registration"),
	path('login',views.user_login, name="login"),
	path('logout',views.user_logout, name="logout"),
	path('',views.home, name="home"),
]