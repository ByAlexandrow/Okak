from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagerOrReadOnlyStatus(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_authenticated:
            return False
        
        if user.team.title.lower() == 'Менеджер':
            return True
        
        if request.method in SAFE_METHODS or request.method in ('PATCH', 'PUT'):
            return True
        return False

    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.team.title.lower() == 'Менеджер':
            return True
        
        if request.method in SAFE_METHODS or request.method in ('PATCH', 'PUT'):
            return True
        return False
