from rest_framework.permissions import BasePermission
from apps.profiles.models import Profile


class IsPhotographer(BasePermission):
    def has_permission(self, request, view):
        try:
            profile = Profile.objects.get(user=request.user)
            return profile.is_photographer
        except Profile.DoesNotExist:
            return False