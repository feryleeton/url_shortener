from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or admin users to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        else:
            return obj.user == request.user
