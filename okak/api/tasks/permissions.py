from rest_framework.permissions import BasePermission


class IsManagerOrReadOnlyStatus(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.team.title.lower() == 'Менеджер':
            return True
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return True
