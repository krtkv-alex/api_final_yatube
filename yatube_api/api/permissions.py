from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    message = 'Вы не являетесь автором поста.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
