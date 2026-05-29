from rest_framework import permissions


class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
