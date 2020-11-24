from django.shortcuts import render
from .models import Profile


def my_profile_view(request):
    """Main user view"""

    obj = Profile.objects.get(user=request.user)

    context = {"obj": obj}
    return render(request, "profiles/my_profile.html", context)
