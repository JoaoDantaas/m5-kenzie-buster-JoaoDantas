from rest_framework import permissions

class PermissionIsSuper(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False

class PermissionToken(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

        return False