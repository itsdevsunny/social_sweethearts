from django.urls import path, include, re_path

from django.contrib.auth import views as auth_views

app_name = 'accounts'

from accounts import views

urlpatterns = [
	re_path(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
	re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	path('profile/', views.Profile, name='profile'),
	path('profile/disconnect/', views.FacebookProfileDisconnect, name='profile-disconnect'),
]