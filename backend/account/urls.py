from django.urls import path

from account import views
from .views import AgentsListView, ManagersListView, UserProfileView


urlpatterns = [
    path('registration',views.registration, name="registration"),
	path('login',views.user_login, name="login"),
	path('logout',views.user_logout, name="logout"),
	path('',views.dashboard, name="dashboard"),
    path('api/agents', AgentsListView.as_view(), name='agents-list'),
    path('api/managers', ManagersListView.as_view(), name='managers-list'),
	path('api/get_user_profile/', UserProfileView.as_view(), name='get_user_profile'),
	path('api/get-auth-token/', views.get_auth_token, name='get-auth-token'),
]