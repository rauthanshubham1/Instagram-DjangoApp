from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/login/", views.user_login, name="login"),
    path("accounts/register/", views.register, name="register"),
    path("accounts/<int:user_id>/", views.profile, name="profile"),
    path("accounts/feed", views.feed, name="feed"),
    path("accounts/add_comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path("accounts/toggle_like/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path("accounts/update_profile_picture/", views.update_profile_picture, name="update_profile_picture"),
    path("accounts/addpost/", views.addpost, name="addpost"),
    path("accounts/friends/", views.friends, name="friends"),
    path("accounts/follow/<int:user_id>/", views.followUser, name="follow"),
    path("accounts/logout/", views.user_logout, name="logout"),
]


