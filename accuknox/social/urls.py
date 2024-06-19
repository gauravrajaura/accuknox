
from django.urls import path

from accuknox.social.api.views import FriendRequestView, UserSearchView

app_name = 'social'

urlpatterns = [
    path("users/", UserSearchView.as_view(), name="user_search"),
    path(
        "friend-request/<int:pk>/",
        FriendRequestView.as_view({"delete": "destroy", "patch": "update"}),
    ),  
    path(
        "friend-request/",
        FriendRequestView.as_view({"post": "create", "get": "list"}),
    ),      
]