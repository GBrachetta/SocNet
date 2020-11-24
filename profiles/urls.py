from django.urls import path
from .views import (
    invites_received_view,
    my_profile_view,
    profiles_list_view,
    invites_profiles_list_view,
)

app_name = "profiles"

urlpatterns = [
    path("myprofile/", my_profile_view, name="my-profile-view"),
    path("my-invites/", invites_received_view, name="my-invites-view"),
    path("all-profiles/", profiles_list_view, name="all-profiles-view"),
    path("to-invite/", invites_profiles_list_view, name="to-invite-view"),
]
