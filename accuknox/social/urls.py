
from django.urls import path

from accuknox.social.api.views import UserSearchView

app_name = 'social'

urlpatterns = [
    path("users/", UserSearchView.as_view(), name="user_search"),
]