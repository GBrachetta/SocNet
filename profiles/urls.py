from django.urls import path

from .views import (
    ProfileDetailView,
    ProfileListView,
    accept_invitation,
    invites_profiles_list_view,
    invites_received_view,
    my_profile_view,
    reject_invitation,
    remove_from_friends,
    send_invitation,
)

app_name = "profiles"

urlpatterns = [
    path("", ProfileListView.as_view(), name="all-profiles-view"),
    path("myprofile/", my_profile_view, name="my-profile-view"),
    path("my-invites/", invites_received_view, name="my-invites-view"),
    path("to-invite/", invites_profiles_list_view, name="to-invite-view"),
    path("send-invite/", send_invitation, name="send-invite"),
    path("remove-friend/", remove_from_friends, name="remove-friend"),
    path("<slug>", ProfileDetailView.as_view(), name="profile-detail-view"),
    path("my-invites/accept", accept_invitation, name="accept-invite"),
    path("my-invites/reject", reject_invitation, name="reject-invite"),
]
